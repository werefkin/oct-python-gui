import sys
from proc_ui import Ui_MainWindow
from threading import Lock      # TO QUEUE THREADS FOR BUFFER_DATA (NOT USED)
from datetime import datetime
import time
import numpy as np
from oct_lib import remap_to_k, scanProcess, norma
import serial
import serial.tools.list_ports
import warnings
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtCore import Slot
import qtmodern.styles
import qtmodern.windows
from help_ui import Ui_HelpWindow
import scipy.signal as scisig
from scipy.signal import decimate
import tifffile as tif
import os
import PySide2
from shared_vars import SharedVariables
from get_buffer_thread import GetBufferThread


dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
data_lock = Lock()  # TO QUEUE THREADS FOR BUFFER_DATA (NOT USED)


class win(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # GLOBALS
        # Global variables -- shared as they are USEB BY SEVERAL THREADS
        global wave_left
        global wave_right
        global gaussian_sigma
        global reference_spectrum
        global avg_num
        global ref_avg_num
        global x_step
        global ystep
        global xstart_coordinate
        global xstop_coordinate
        global ystart_coordinate
        global ystop_coordinate
        global idle_time
        global data
        global samples_num
        global b_scan
        global gaussian_pos
        global interm_output
        global gaussian_window
        global raw_data
        global directory
        global flag, measurement_flag, inloop_flag
        global decimation_factor

        self.shared_vars = SharedVariables()
        # General parameters
        if 'reference_spectrum' not in globals():
            reference_spectrum = np.load('./reference/ref.npy')
        # PRESET PARAMETERS
        wave_left = 3235.6
        wave_right = 4472.27
        avg_num = 3  # Number of averaged measurements
        ref_avg_num = 50
        x_step = 0.04
        xstart_coordinate = 3
        xstop_coordinate = 0
        idle_time = 0.05
        gaussian_pos = 0
        gaussian_sigma = 1500  # sigma, gaussian window parameter
        flag = 0  # General flag showing if App is running
        measurement_flag = 1
        inloop_flag = 1
        raw_data = np.zeros([100, 100])
        samples_num = 16384
        decimation_factor = 20  # to downsample Live signals (more efficient plotting)
        # POST PROCESSING PRESET
        gaussian_window = np.exp(-1 / 2 * ((np.linspace(-(samples_num - 1) / 2,
                                 (samples_num - 1) / 2, samples_num) - gaussian_pos) / (4 * gaussian_sigma))**2)
        # gaussian_window = np.interp(
        #     gaussian_window, (gaussian_window.min(), gaussian_window.max()), (-1, 1))


#       THREADS
        self.buffer_thread = GetBufferThread(self.shared_vars)
        self.save_thread = SaveDataThread(self)
        self.bscan_measurement_thread = BScanMeasureThread(self.shared_vars)
        self.cscan_measurement_thread = VolumeScanningThread(self.shared_vars)

        self.save_params_thread = SaveParamsThread(self)

        self.referencing_thread = GetReferenceThread(self.shared_vars)
        self.sys_init_thread = InitializationThread(self.shared_vars)
        self.ystage_init_thread = YstageInitThread(self)
        self.post_process_thread = PostProcessingThread(self)
        self.y_stage_up = YMoveUpByThread(self)
        self.y_stage_down = YMoveDownByThread(self)
        self.y_axis_move_to = YPositionToThread(self)
        self.x_axis_move_to = XPositionToThread(self)

        # self.buffer_thread .start()

#        BUTTONS SIGNALS
        self.ui.InitButton.clicked.connect(self.set_init_parameters)
        self.ui.InitButton.clicked.connect(
            self.sys_init_thread.start)
        self.ui.InitializeYstageButton.clicked.connect(
            self.ystage_init_thread.start)
        self.ui.YStageUpButton.clicked.connect(self.y_stage_up.start)
        self.ui.YStageDownButton.clicked.connect(self.y_stage_down.start)
        self.ui.YStageMoveToButton.clicked.connect(self.get_startpos)
        self.ui.YStageMoveToButton.clicked.connect(self.y_axis_move_to.start)
        self.ui.Button_XMoveTo.clicked.connect(self.get_startpos)
        self.ui.Button_XMoveTo.clicked.connect(self.x_axis_move_to.start)

        self.ui.InitButton.clicked.connect(self.set_acq_parameters)
        self.ui.StopButton.clicked.connect(self.stop_measurements)

        self.ui.FolderButton.clicked.connect(self._open_file_dialog)
        self.ui.Bscan_MeasureButton.clicked.connect(self.set_octparameters)
        self.ui.Bscan_MeasureButton.clicked.connect(self.bscan_measurement_thread.start)

        self.ui.StartCscanButton.clicked.connect(self.set_octparameters)
        self.ui.StartCscanButton.clicked.connect(
            self.set_postprocessparameters)
        self.ui.StartCscanButton.clicked.connect(self.set_cscan_parameters)
        self.ui.StartCscanButton.clicked.connect(
            self.cscan_measurement_thread.start)

        self.ui.Bscan_MeasureButton.clicked.connect(self.status_ui_measurements_started)
        self.ui.ReferenceButton.clicked.connect(self.set_octparameters)
        self.ui.ReferenceButton.clicked.connect(self.referencing_thread.start)
        self.ui.PlotButton.clicked.connect(self.graph)
        self.ui.ApplyButton.clicked.connect(self.set_acq_parameters)
        self.ui.SetOCTParamsButton.clicked.connect(self.set_octparameters)
        self.ui.AveragingCheckBox.stateChanged.connect(self.set_octparameters)
        self.ui.SetProcParamsButton.clicked.connect(
            self.set_postprocessparameters)
        self.ui.ResetReferenceButton.clicked.connect(self.reset_ref)
        self.ui.SaveButton.clicked.connect(self.save)
        self.ui.SaveButton.clicked.connect(self.save_thread.start)

        self.ui.SetRangeButton.clicked.connect(self.resarray)
        self.ui.SetRangeButton.clicked.connect(self.buffer_thread.start)
        self.ui.StopAcqButton.clicked.connect(self.stop_spectrometer)
        self.ui.actionAbout.triggered.connect(self.openWindow)
        self.ui.ApplyProcButton.clicked.connect(self.post_process_thread.start)
        self.ui.SetRangeButton.clicked.connect(self.reset_parameters)
        self.ui.actionSave.triggered.connect(self.save_params_thread.start)


#        OTHER SIGNAL-SLOT CONNECTIONS
        self.referencing_thread.refprog.connect(self.refprogress)
        self.referencing_thread.refdone.connect(self.plotref)
        self.bscan_measurement_thread.measprog.connect(self.measprogress)
        self.bscan_measurement_thread.mdat.connect(self.graph)
        self.bscan_measurement_thread.mdat.connect(self.status_ui_measurements_done)
        self.post_process_thread.request_parameters.connect(
            self.set_postprocessparameters)

        self.sys_init_thread.initdone.connect(self.activatemeas)
        self.ystage_init_thread.initdone.connect(self.activate3Dmeas)

        self.sys_init_thread.initdone.connect(
            self.buffer_thread .start)
        self.sys_init_thread.init_status.connect(self.addlogline)

        self.ystage_init_thread.init_status.connect(self.addlogline)

        self.bscan_measurement_thread.meas_status.connect(self.addlogline)

        self.cscan_measurement_thread.meas_status.connect(self.addlogline)
        self.cscan_measurement_thread.mdat.connect(self.graph)
        self.cscan_measurement_thread.measprog.connect(self.measprogress)

        self.save_thread.status.connect(self.addlogline)

        self.y_stage_up.status.connect(self.addlogline)
        self.y_stage_down.status.connect(self.addlogline)
        self.y_axis_move_to.status.connect(self.addlogline)
        self.x_axis_move_to.status.connect(self.addlogline)

#        PLOTS
        b_scan = np.load('./logo/preset.npy')[:155, :]
        self.ui.BscanWidget.show()
        self.ui.BscanWidget.setImage(20 * np.log10(np.rot90(b_scan) + 0.1))
        self.ui.BscanWidget.view.setAspectLocked(ratio=0.45)
        self.ui.BscanWidget.view.setBackgroundColor(None)
        self.ui.raw_signal_plot.addLegend()
        self.ui.raw_signal_plot.setBackground((35, 35, 35))
        self.ui.curve = self.ui.raw_signal_plot.plot(
            decimate(
                np.zeros(samples_num),
                decimation_factor,
                axis=0),
            pen={
                'color': (
                    252,
                    72,
                    72),
                'width': 1.5},
            name='Live')
        self.ui.refcurve = self.ui.raw_signal_plot.plot(
            decimate(
                reference_spectrum,
                decimation_factor,
                axis=0),
            pen={
                'color': (
                    40,
                    198,
                    48),
                'width': 2},
            name='Reference')
        self.ui.gaussian = self.ui.raw_signal_plot.plot(
            decimate(
                gaussian_window,
                decimation_factor,
                axis=0),
            pen={
                'color': (
                    252,
                    142,
                    51),
                'width': 2},
            name='Gaussian window')
        self.ui.raw_signal_plot.setYRange(-1, 1)
        # self.ui.raw_signal_plot.setXRange(0,800)
        self.ui.raw_signal_plot.setClipToView(True)


#        TIMER AND LIVE SIGNAL UPD
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100)

#        RADIOBUTTONS
        self.ui.Preset2Radio.toggled.connect(self.preset2_mode)
        self.ui.Preset1Radio.toggled.connect(self.preset1_mode)

        self.variable = 10
        global param1
        param1 = self.ui.param1.text()

    def stop_measurements(self):
        global measurement_flag, inloop_flag
        measurement_flag = 0
        inloop_flag = 0

    def _open_file_dialog(self):
        global directory
        directory = str(QtWidgets.QFileDialog.getExistingDirectory())
        print(directory)
        self.ui.FolderLine.setText('{}'.format(directory))

    def openWindow(self):
        self.about = QtWidgets.QMainWindow()
        self.uis = Ui_HelpWindow()
        self.uis.setupUi(self.about)
        self.uis.OKCloseButton.clicked.connect(self.closeWindow)
        self.about = qtmodern.windows.ModernWindow(self.about)
        qr = self.about.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.about.move(qr.topLeft())
        self.about.show()

    def closeWindow(self):
        print('q')
        self.about.close()

    def update(self):
        #        self.value=np.random.rand(510)
        self.ui.curve.setData(decimate(self.shared_vars.buffer_signal, decimation_factor, axis=0))

    def set_cscan_parameters(self):
        global ystep
        global ystart_coordinate
        global ystop_coordinate

        ystep = float(self.ui.y_step.text())
        ystart_coordinate = float(self.ui.ui_y_start_pos.text())
        ystop_coordinate = float(self.ui.ui_y_stop_pos.text())

    def activatemeas(self):
        self.ui.Bscan_MeasureButton.setEnabled(True)
        self.ui.SaveButton.setEnabled(True)
        self.ui.ReferenceButton.setEnabled(True)
        self.ui.Button_XMoveTo.setEnabled(True)

    def activate3Dmeas(self):
        self.ui.StartCscanButton.setEnabled(True)
        self.ui.YStageUpButton.setEnabled(True)
        self.ui.YStageDownButton.setEnabled(True)
        self.ui.YStageMoveToButton.setEnabled(True)

    def reset_ref(self):
        global reference_spectrum
        reference_spectrum = np.zeros(samples_num)
        self.ui.refcurve.setData(decimate(reference_spectrum, decimation_factor, axis=0))

    def measprogress(self, pbar):
        self.ui.scanprogressBar.setValue(int(pbar))

    @Slot(object)
    def addlogline(self, status_text):
        self.ui.logbrowser.append(status_text)

    def save(self):
        global filename
        global logcoeff
        filename = self.ui.filenameline.text()
        logcoeff = float(self.ui.log10_coef.text())

    def refprogress(self, rpbar):
        self.ui.refprogressBar.setValue(int(rpbar))

    def plotref(self):
        global reference_spectrum
        self.ui.refcurve.setData(decimate(reference_spectrum, decimation_factor, axis=0))

    def graph(self):
        self.ui.BscanWidget.setImage(
            20 *
            np.log10(
                np.rot90(b_scan) +
                float(
                    self.ui.log10_coef.text())))
        self.ui.BscanWidget.view.setAspectLocked(
            ratio=float(self.ui.aspect_ratio.text()))
        self.ui.logbrowser.append('Data visualized successfully')

    def set_acq_parameters(self):
        global delay
        global param1
        param1 = self.ui.param1.text()
        print(param1)

    def set_init_parameters(self):
        # READ OUT GUI PARAMS TO SET THEM

        global delay
        # Part of buff <samples_num>
        self.shared_vars.sample_min = int(self.ui.sampling_start_ui.text())
        self.shared_vars.sample_max = int(self.ui.sampling_stop_ui.text())
        delay = str(self.ui.trig_delay.text())

    def reset_parameters(self):
        # READ OUT GUI PARAMS TO SET THEM
        global samples_num
        global refern
        global scanrange
        global refern
        global data
        global interm_output
        global outputfft
        global delay

        # Part of buff <samples_num>
        self.shared_vars.sample_min = int(self.ui.sampling_start_ui.text())
        self.shared_vars.sample_max = int(self.ui.sampling_stop_ui.text())
        samples_num = self.shared_vars.sample_max - self.shared_vars.sample_min
        print(samples_num)
        scanrange = np.flip(np.arange(xstop_coordinate, xstart_coordinate + x_step, x_step), 0)
        refern = np.zeros([ref_avg_num, samples_num])
        # spectarr = (c_float*510)()
        data = np.zeros([samples_num, avg_num])
        interm_output = np.zeros([samples_num, len(scanrange)])
        outputfft = np.zeros([samples_num, len(scanrange)])
        gaussian_window = np.exp(-1 / 2 * ((np.linspace(-(samples_num - 1) / 2,
                                 (samples_num - 1) / 2, samples_num) - gaussian_pos) / (4 * gaussian_sigma))**2)
        # gaussian_window = np.interp(
        #     gaussian_window, (gaussian_window.min(), gaussian_window.max()), (-1, 1))
        self.ui.gaussian.setData(decimate(gaussian_window, decimation_factor, axis=0))
        delay = str(self.ui.trig_delay.text())

    def get_startpos(self):
        global ystart_coordinate
        ystart_coordinate = float(self.ui.ui_y_start_pos.text())
        global xstart_coordinate
        xstart_coordinate = float(self.ui.x_start_pos_ui.text())

    def set_octparameters(self):
        global avg_num
        global ref_avg_num
        global x_step
        global xstart_coordinate
        global xstop_coordinate
        global idle_time
        global data
        global refern
        global scanrange
        global outputfft
        global interm_output
        global gaussian_sigma
        global gaussian_pos
        global ystep
        global ystart_coordinate
        global ystop_coordinate

        if self.ui.AveragingCheckBox.isChecked():
            print('Averaging mode')
            avg_num = int(self.ui.avg_num_ui.text())  # Number of averaged pixels
        else:
            print('No averaging')
            avg_num = 1  # Number of averaged pixels

        ref_avg_num = int(self.ui.ref_avg_num_ui.text())
        print(ref_avg_num)
        x_step = float(self.ui.x_step_ui.text())
        xstart_coordinate = float(self.ui.x_start_pos_ui.text())
        xstop_coordinate = float(self.ui.x_stop_pos_ui.text())

        ystep = float(self.ui.y_step.text())
        ystart_coordinate = float(self.ui.ui_y_start_pos.text())
        ystop_coordinate = float(self.ui.ui_y_stop_pos.text())

        idle_time = float(self.ui.a_idle_time.text())

        data = np.zeros([samples_num, avg_num])
        refern = np.zeros([ref_avg_num, samples_num])
        scanrange = np.flip(np.arange(xstop_coordinate, xstart_coordinate + x_step, x_step), 0)

        interm_output = np.zeros([samples_num, len(scanrange)])
        outputfft = np.zeros([samples_num, len(scanrange)])

    def set_postprocessparameters(self):

        global wave_left
        global wave_right
        global gaussian_sigma
        global gaussian_pos
        wave_left = int(self.ui.wave_left_ui.text())
        wave_right = int(self.ui.wave_right_ui.text())
        gaussian_sigma = int(self.ui.gaussian_std_ui.text())
        gaussian_pos = int(self.ui.gaussian_pos_ui.text())
        self.ui.logbrowser.append(
            '\nBandwidth SET, LOW Wavelength: ' + str(wave_left))
        self.ui.logbrowser.append('Bandwidth SET, HIGH Wavelength: ' + str(wave_right))
        self.ui.logbrowser.append('Gaussian window width (STD): ' + str(gaussian_sigma))
        self.ui.logbrowser.append(
            'Gaussian window position: ' + str(gaussian_pos) + '\n')

        gaussian_window = np.exp(-1 / 2 * ((np.linspace(-(samples_num - 1) / 2,
                                 (samples_num - 1) / 2, samples_num) - gaussian_pos) / (4 * gaussian_sigma))**2)
        # gaussian_window = np.interp(
        #     gaussian_window, (gaussian_window.min(), gaussian_window.max()), (-1, 1))
        self.ui.gaussian.setData(decimate(gaussian_window, decimation_factor, axis=0))

    def preset2_mode(self):
        global wave_left
        global wave_right
        global gaussian_sigma
        global gaussian_pos
        wave_left = 1850
        wave_right = 2150
        gaussian_sigma = 200
        gaussian_pos = 0
        self.ui.wave_right_ui.setText(str(wave_right))
        self.ui.wave_left_ui.setText(str(wave_left))
        self.ui.gaussian_std_ui.setText(str(gaussian_sigma))
        self.ui.aspect_ratio.setText('1')
        gaussian_window = np.exp(-1 / 2 * ((np.linspace(-(samples_num - 1) / 2,
                                 (samples_num - 1) / 2, samples_num) - gaussian_pos) / (4 * gaussian_sigma))**2)
        # gaussian_window = np.interp(
        #     gaussian_window, (gaussian_window.min(), gaussian_window.max()), (-1, 1))
        self.ui.gaussian.setData(decimate(gaussian_window, decimation_factor, axis=0))

    def preset1_mode(self):
        global wave_left
        global wave_right
        global gaussian_sigma
        global gaussian_pos
        wave_left = 3720
        wave_right = 4200
        gaussian_sigma = 1000
        gaussian_pos = 0
        self.ui.wave_right_ui.setText(str(wave_right))
        self.ui.wave_left_ui.setText(str(wave_left))
        self.ui.gaussian_std_ui.setText(str(gaussian_sigma))
        self.ui.gaussian_pos_ui.setText(str(gaussian_pos))
        self.ui.aspect_ratio.setText('0.5')
        gaussian_window = np.exp(-1 / 2 * ((np.linspace(-(samples_num - 1) / 2,
                                 (samples_num - 1) / 2, samples_num) - gaussian_pos) / (4 * gaussian_sigma))**2)
        # gaussian_window = np.interp(
        #     gaussian_window, (gaussian_window.min(), gaussian_window.max()), (-1, 1))
        self.ui.gaussian.setData(decimate(gaussian_window, decimation_factor, axis=0))

    def stop_spectrometer(self):
        print('Stopped')
        print(self.shared_vars.flag)
        self.shared_vars.flag = 1

    def resarray(self):
        self.ui.logbrowser.append('Parameters (re)set, (re)start')
        self.shared_vars.flag = 0

    def status_ui_measurements_started(self):
        self.ui.InitButton.setEnabled(False)
        self.ui.SetOCTParamsButton.setEnabled(False)
        self.ui.ApplyProcButton.setEnabled(False)

    def status_ui_measurements_done(self):
        self.ui.InitButton.setEnabled(True)
        self.ui.SetOCTParamsButton.setEnabled(True)
        self.ui.ApplyProcButton.setEnabled(True)

    def closeEvent(self, event):
        global flag
        reply = QMessageBox.question(self, 'Exit', 'Do you want to exit?')
        if reply == QMessageBox.Yes:
            event.accept()
            flag = 1
            self.shared_vars.flag = 1
            # self.ui.BscanWidget.deleteLater()
            # self.ui.curve.deleteLater()
            time.sleep(1)
            self.ui.BscanWidget.setParent(None)
            print('Close')
            QApplication.quit()
        else:
            event.ignore()


"""
THREADS
"""


class GetReferenceThread(QtCore.QThread):

    refprog = QtCore.Signal(object)
    refdone = QtCore.Signal(object)

    def __init__(self, shared_vars):
        super().__init__()
        self.shared_vars = shared_vars

    def run(self):
        global measurement_flag, reference_spectrum
        for i in range(0, len(refern)):
            time.sleep(idle_time)
            if measurement_flag == 0:
                measurement_flag = 1
                break
            refern[i, :] = self.shared_vars.buffer_signal

            self.refprogress = (i + 1) / len(refern) * 100
            self.refprog.emit(self.refprogress)

        reference_spectrum = np.mean(refern[:i, :], 0)
        self.refdone.emit(self.refprogress)


class YMoveUpByThread(QtCore.QThread):
    status = QtCore.Signal(object)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        print('Moved up by 0.5 mm')
        self.msg = 'Moved up by 0.5 mm'
        self.status.emit(self.msg)


class YMoveDownByThread(QtCore.QThread):
    status = QtCore.Signal(object)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        print('Moved down by 0.5 mm')
        self.msg = 'Moved down by 0.5 mm'
        self.status.emit(self.msg)


class YPositionToThread(QtCore.QThread):
    status = QtCore.Signal(object)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        global ystart_coordinate
        self.msg = 'Moved to start Y position'
        self.status.emit(self.msg)


class XPositionToThread(QtCore.QThread):
    status = QtCore.Signal(object)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        global xstart_coordinate
        self.msg = 'Moved to start X position: ' + str(xstart_coordinate)
        self.status.emit(self.msg)


class VolumeScanningThread(QtCore.QThread):
    measprog = QtCore.Signal(object)
    mdat = QtCore.Signal(object)
    meas_status = QtCore.Signal(object)

    def __init__(self, shared_vars):
        super().__init__()
        self.shared_vars = shared_vars

    def run(self):
        start_time = time.time()
        global b_scan
        global scanf
        global scans
        global flag
        global measurement_flag
        global ystep
        global ystart_coordinate
        global ystop_coordinate
        global avg_num
        global ref_avg_num
        global x_step
        global xstart_coordinate
        global xstop_coordinate
        global idle_time
        global data
        global refern
        global scanrange
        global outputfft
        global interm_output
        global gaussian_sigma
        global gaussian_pos
        global wave_left
        global wave_right
        global b_scan
        global flag
        global measurement_flag

        yscanrange = np.flip(np.arange(ystop_coordinate, ystart_coordinate + ystep, ystep), 0)

        ascanav = np.zeros([samples_num, avg_num, len(scanrange)])

        vscan = np.zeros([len(yscanrange), 512, len(scanrange)])

        totalmeasurements = len(yscanrange) * len(scanrange)

        # START MEASUREMENT
        start_time = time.time()
        len_counter = 1
        z_counter = 1

        for zpos in range(0, len(yscanrange)):

            print(yscanrange[zpos])
            print(zpos)

            # motor.move_to(yscanrange[zpos], True)

            if measurement_flag == 0:
                measurement_flag = 1
                break

            for itn in range(0, len(scanrange)):
                print('Position:', round(scanrange[itn], 3), 'mm')
                if measurement_flag == 0:
                    break

                for i in range(0, avg_num):
                    print(
                        'Y-STEPNUM: ',
                        zpos,
                        ' Position:',
                        round(
                            scanrange[itn],
                            3),
                        'mm ',
                        "Spectrum number: ",
                        i)
                    data[:, i] = np.flip(self.shared_vars.buffer_signal, 0)
                    # FOR FUTHER FFT AVERAGING
                    ascanav[:, i, itn] = np.flip(self.shared_vars.buffer_signal, 0)
                    time.sleep(idle_time)
                    if flag != 0:
                        break
                interm_output[:, itn] = np.mean(data, 1)
                avft = np.flip(np.rot90(data, 1), 1)
                outputfft[:, itn] = np.mean(scanProcess(np.flip(remap_to_k(
                    avft, reference_spectrum, wave_left, wave_right, cal_vector, boundaries), 0), gaussian_window), 0)

                len_counter = len_counter + 1

                self.progress = 100 * \
                    (len_counter + z_counter) / totalmeasurements
                self.measprog.emit(self.progress)
                if flag != 0:
                    break
            topost = np.flip(np.rot90(interm_output, 1), 1)
            if flag != 0:
                break

            # PROCESS
            b_scan = scanProcess(
                np.flip(
                    remap_to_k(
                        topost,
                        reference_spectrum,
                        wave_left,
                        wave_right,
                        cal_vector,
                        boundaries),
                    0),
                gaussian_window)
            scanf = np.rot90(b_scan)

            vscan[zpos, :, :] = scanf[int(samples_num / 2):int(samples_num / 2) + 512, :]
            scans = vscan
            b_scan = np.flip(np.moveaxis(
                np.flip(vscan[:zpos + 1, :, :], 0), -1, 0), 1)
            z_counter = z_counter + 1
            if np.shape(b_scan)[1] > 0:
                self.mdat.emit(self.progress)
                print(np.shape(b_scan))

        # motor.move_to(yscanrange[0])

        global vscancheck
        vscancheck = vscan
        # b_scan=vscan
        b_scan = np.moveaxis(np.flip(vscan, 0), -1, 0)
        print('3D measurement completed')
        self.ms_msg = '3D b_scan DONE in ' + \
            "--- %s seconds ---" % (time.time() - start_time)
        self.meas_status.emit(self.ms_msg)
        self.progress = 100
        self.measprog.emit(self.progress)


class BScanMeasureThread(QtCore.QThread):
    measprog = QtCore.Signal(object)
    mdat = QtCore.Signal(object)
    meas_status = QtCore.Signal(object)

    def __init__(self, shared_vars):
        super().__init__()
        self.shared_vars = shared_vars

    def run(self):
        err = 0
        start_time = time.time()
        global outputfft
        global b_scan
        global scanf
        global scans
        global flag
        global measurement_flag, inloop_flag
        global gaussian_window
        if len(data) == len(reference_spectrum):
            self.ms_msg = 'Measurements started...\n' + 'b_scan length: ' + \
                str(xstart_coordinate - xstop_coordinate) + 'mm\n' + 'Averaging: ' + str(avg_num)
            self.meas_status.emit(self.ms_msg)
            for itn in range(0, len(scanrange)):
                print(
                    'Position: ',
                    round(
                        scanrange[itn],
                        2),
                    'mm; Errors: ',
                    err,
                    '; Av.avg_num:',
                    avg_num,
                    ';  Gaussian window:',
                    gaussian_sigma,
                    ' WinWidth: ',
                    gaussian_pos)
    #            position=round(scanrange[itn],3)
                self.progress = 100 * (itn + 1) / len(scanrange)
                self.measprog.emit(self.progress)

                if measurement_flag == 0:
                    measurement_flag = 1
                    break
                for i in range(0, avg_num):  # Averaging
                    if flag != 0:
                        break
                    if inloop_flag == 0:
                        inloop_flag = 1
                        break
                    time.sleep(idle_time)
                    data[:, i] = np.flip(self.shared_vars.buffer_signal, 0)
                interm_output[:, itn] = np.mean(data, 1)

                avft = np.flip(np.rot90(data, 1), 1)
                outputfft[:, itn] = np.mean(scanProcess(np.flip(remap_to_k(
                    avft, reference_spectrum, wave_left, wave_right, cal_vector, boundaries), 0), gaussian_window), 0)
                if flag != 0:
                    break
            topost = np.flip(np.rot90(interm_output, 1), 1)
            global raw_data
            raw_data = np.copy(topost)

            # PROCESS
            b_scan = scanProcess(
                np.flip(
                    remap_to_k(
                        topost,
                        reference_spectrum,
                        wave_left,
                        wave_right,
                        cal_vector,
                        boundaries),
                    0),
                gaussian_window)
            scanf = np.rot90(b_scan)

            # AVERAGE WITH MEAN FOURIER SPACE
            cuscus = np.average([norma(scanf[int(samples_num /
                                                 2):int(samples_num /
                                                        2 +
                                                        512), :], norma=0), norma(outputfft[int(samples_num /
                                                                                                2 +
                                                                                                1):int(samples_num /
                                                                                                       2 +
                                                                                                       512 +
                                                                                                       1), :], norma=0)], 0)
            cuscus = norma(cuscus, norma=0)

    #        b_scan=cuscus[:-100,:]
            purescn = norma(scanf, norma=0)
            pureftscn = norma(outputfft, norma=0)

            global scans
            scans = np.array([cuscus, purescn[int(samples_num /
                                                  2):int(samples_num /
                                                         2 +
                                                         512), :], pureftscn[int(samples_num /
                                                                                 2 +
                                                                                 1):int(samples_num /
                                                                                        2 +
                                                                                        512 +
                                                                                        1), :]])

            # scans=np.array([cuscus[int(samples_num/2):int(samples_num/2+800),:],purescn[int(samples_num/2):int(samples_num/2+800),:],pureftscn[int(samples_num/2):int(samples_num/2+800),:]])
            b_scan = np.moveaxis(np.flip(scans, 0), -1, 0)
            print("--- %s seconds ---" % (time.time() - start_time))
            # np.save('topost.npy', topost)
            self.ms_msg = 'DONE in ' + \
                "--- %s seconds ---" % (time.time() - start_time)
            self.meas_status.emit(self.ms_msg)
            self.mdat.emit(self.progress)
        else:
            self.ms_msg = 'ERROR - Referencing is needed'
            self.meas_status.emit(self.ms_msg)


class PostProcessingThread(QtCore.QThread):
    request_parameters = QtCore.Signal(object)

    def __init__(self, parent=win):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        self.request_parameters.emit(self)
        print(wave_left)
        print(wave_right)
        print(gaussian_sigma)
        print(gaussian_pos)
        # PROCESS
#        local_outputfft=raw_fftout
        global raw_data
        local_topost = np.copy(raw_data)
        local_scan = scanProcess(
            np.flip(
                remap_to_k(
                    local_topost,
                    reference_spectrum,
                    wave_left,
                    wave_right,
                    cal_vector,
                    boundaries),
                0),
            gaussian_window)
        local_scanf = np.rot90(local_scan)
        # AVERAGE WITH MEAN FOURIER SPACE
#        local_cuscus=np.average([norma(local_scanf[256:-1,:],norma=0),norma(local_outputfft[257:,:],norma=0)],0)
#        local_cuscus=norma(local_cuscus,norma=0)
        local_purescn = local_scanf[int(samples_num / 2):int(samples_num / 2 + 512), :]
#        local_pureftscn=norma(local_outputfft[257:,:],norma=0)
#        local_scans=np.array([local_cuscus[:-100,:],local_purescn[:-100,:],local_pureftscn[:-100,:]])
        global b_scan
        b_scan = np.flip(local_purescn, 1)
        del local_topost


class YstageInitThread(QtCore.QThread):
    initdone = QtCore.Signal(object)
    init_status = QtCore.Signal(object)

    def __init__(self, parent=win):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        try:
            print('Y stage initialization')
            # Initialize your YStage here
            print('Y stage initialized')

            self.init_msg = 'Y stage is initialized'
            self.init_status.emit(self.init_msg)
            self.initdone.emit(self)

        except BaseException:
            self.init_msg = 'Y stage is not found'
            self.init_status.emit(self.init_msg)


class InitializationThread(QtCore.QThread):
    initdone = QtCore.Signal(object)
    init_status = QtCore.Signal(object)

    def __init__(self, shared_vars):
        super().__init__()
        self.shared_vars = shared_vars

    def run(self):
        global shutt
        global samples_num
        global scanrange
        global refern
        global data
        global interm_output
        global outputfft
        global delay
        global cal_vector
        global boundaries

        try:
            cal_vector = np.load('calibration_vector.npy')
            boundaries = np.load('boundaries.npy')
            print('Calibration vector loaded')
            self.init_msg = 'Calibration vector loaded'
            self.init_status.emit(self.init_msg)
        except BaseException:
            cal_vector = None
            boundaries = None
            print('Calibration vector not found')
            self.init_msg = 'Calibration vector not found'
            self.init_status.emit(self.init_msg)
            pass

        # #DAQ CONFIGURATION
        # define here your signal source

        # Number of samples
        samples_num = self.shared_vars.sample_max - self.shared_vars.sample_min
        self.init_msg = '\nNumber of samples: ' + str(samples_num)
        self.init_status.emit(self.init_msg)
        b, a = scisig.butter(4, 0.0005, btype='highpass')

        # GLOBAL EMPTHY VARIABLES
        scanrange = np.flip(np.arange(xstop_coordinate, xstart_coordinate + x_step, x_step), 0)
        refern = np.zeros([ref_avg_num, samples_num])
        position = 0
        # spectarr = (c_float*510)()
        data = np.zeros([samples_num, avg_num])
        interm_output = np.zeros([samples_num, len(scanrange)])
        outputfft = np.zeros([samples_num, len(scanrange)])

        # STAGE CONFIGURATION
        CONTROLLERNAME = 'C-863.11'
        STAGES = ['M-126.PD1']  # connect stages to axes
        REFMODES = ['FNL', 'FRF']
        velocity = 15
        scanv = 10

        if 'shutt' in locals():
            if shutt.isOpen():
                shutt.close()
        if 'shutt' not in globals():
            try:

                arduino_ports = [
                    p.device
                    for p in serial.tools.list_ports.comports()
                    if 'Arduino' in p.description
                ]
                if not arduino_ports:
                    raise IOError("No Arduino found")
                if len(arduino_ports) > 1:
                    warnings.warn('Multiple Arduinos found - using the first')

                shutt = serial.Serial(arduino_ports[0], 9600, timeout=50)
                time.sleep(1)
                print('\nShutter system is initialized:', shutt.isOpen())
                self.init_msg = 'Shutter system is initialized:' + \
                    str(shutt.isOpen())

            except BaseException:
                print('\nShutter is is not found')
                self.init_msg = 'Shutter system is not found'

            self.init_status.emit(self.init_msg)

        print('\nMoving to start position...')
        print('\nReady to measure...')
        self.init_msg = '\nHardware is successfully initialized\nReady to measure...\n'
        self.init_status.emit(self.init_msg)
        self.initdone.emit(self)


class SaveDataThread(QtCore.QThread):
    status = QtCore.Signal(object)

    def __init__(self, parent=win):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        global scans
        global logcoeff
        global filename
        if 'scans' in globals() and np.mean(scans) != 0:
            try:
                np.save(
                    directory +
                    '/' +
                    filename +
                    datetime.now().strftime('%Y-%m-%d_%H-%M') +
                    '.npy',
                    scans)
                print('Saved as ' + directory + '/' + filename +
                      datetime.now().strftime('%Y-%m-%d_%H-%M') + '.npy')
                # self.ui.logbrowser.append('Saved as '+directory+'/'+filename+datetime.now().strftime('%Y-%m-%d_%H-%M')+'.npy \n')
                self.msg = 'Saved in ' + directory
                self.status.emit(self.msg)
                if np.shape(scans)[0] > 3:
                    scans_to_save = 20 * np.log10(np.copy(scans) + logcoeff)
                    scans_to_save = scans_to_save - np.min(scans_to_save)
                    scans_to_save = scans_to_save / \
                        np.max(scans_to_save) * 65536
                    scans_to_save = scans_to_save[:, :, :]
                    scans_to_save = scans_to_save.astype(np.uint16)
                    try:
                        tif.imwrite(
                            directory +
                            '/' +
                            filename +
                            datetime.now().strftime('%Y-%m-%d_%H-%M') +
                            '.tif',
                            scans_to_save,
                            photometric='minisblack')
                        self.msg = 'Tif volume saved in ' + directory
                        self.status.emit(self.msg)
                    except BaseException:
                        self.msg = 'Tif volume saved in ' + './data_output/'
                        self.status.emit(self.msg)
                        tif.imwrite(
                            './data_output/' +
                            filename +
                            datetime.now().strftime('%Y-%m-%d_%H-%M') +
                            '.tif',
                            scans_to_save,
                            photometric='minisblack')
            except BaseException:
                np.save(
                    './data_output/' +
                    filename +
                    datetime.now().strftime('%Y-%m-%d_%H-%M') +
                    '.npy',
                    scans)
                self.msg = 'Saved in ' + './data_output/'
                self.status.emit(self.msg)
                if np.shape(scans)[0] > 3:
                    scans_to_save = 20 * np.log10(np.copy(scans) + logcoeff)
                    scans_to_save = scans_to_save - np.min(scans_to_save)
                    scans_to_save = scans_to_save / \
                        np.max(scans_to_save) * 65536
                    scans_to_save = scans_to_save[:, :, :]
                    scans_to_save = scans_to_save.astype(np.uint16)
                    self.msg = 'Tif volume saved in ' + './data_output/'
                    self.status.emit(self.msg)
                    tif.imwrite(
                        './data_output/' +
                        filename +
                        datetime.now().strftime('%Y-%m-%d_%H-%M') +
                        '.tif',
                        scans_to_save,
                        photometric='minisblack')
                # self.ui.logbrowser.append('Saved as: '+('./data_output/'+filename+datetime.now().strftime('%Y-%m-%d_%H-%M')+'.npy \n'))
        else:
            print('Empthy data')
            # self.ui.logbrowser.append('b_scan cannot be saved, EmptyData')


class SaveParamsThread(QtCore.QThread):
    status = QtCore.Signal(object)

    def __init__(self, parent=win):
        QtCore.QThread.__init__(self, parent)

    def run(self):

        global wave_left
        global wave_right
        global gaussian_sigma
        global reference_spectrum
        global avg_num
        global ref_avg_num
        global x_step
        global xstart_coordinate
        global xstop_coordinate
        global idle_time
        global data
        global samples_num
        global b_scan
        global gaussian_pos
        global interm_output
        global gaussian_window
        global raw_data
        global flag
        global directory
        global measurement_flag
        global ystep
        global ystart_coordinate
        global ystop_coordinate
        np.save('./reference/ref.npy', reference_spectrum)


if __name__ == "__main__":
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QtCore.QCoreApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
        app.setWindowIcon(QtGui.QIcon("icon.ico"))
    qtmodern.styles.dark(app)
    mwins = win()
    mwins = qtmodern.windows.ModernWindow(mwins)
    qr = mwins.frameGeometry()
    cp = QtWidgets.QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    mwins.move(qr.topLeft())
    mwins.show()
    sys.exit(app.exec_())
