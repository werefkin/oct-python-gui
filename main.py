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
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Slot
import qtmodern.styles
import qtmodern.windows
from help_ui import Ui_HelpWindow
import scipy.signal as scisig
from scipy.signal import decimate
import tifffile as tif
import os
import PySide2

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
        global wh
        global gaw
        global refers
        global num
        global refnum
        global step
        global startp
        global stopp
        global idle_time
        global data
        global px
        global scan
        global posw
        global buffer_signal
        global output
        global gaussian_window
        global rawdat
        global flag
        global directory
        global measurement_flag
        global ystep
        global ystartp
        global ystopp

        # General parameters
        if 'refers' not in globals():
            refers = np.load('./reference/ref.npy')
        buffer_signal = refers
        # PRESET PARAMETERS
        wave_left = 3235.6
        wh = 4472.27
        num = 3  # Number of averaged pixels
        refnum = 50
        step = 0.04
        startp = 3
        stopp = 0
        idle_time = 0.05
        posw = 0
        gaw = 1500  # sigma, gaussian window parameter
        flag = 0
        measurement_flag = 1

        px = 16384
        # POST PROCESSING PRESET
        gaussian_window = np.exp(-1 / 2 * ((np.linspace(-(px - 1) / 2,
                                 (px - 1) / 2, px) - posw) / (4 * gaw))**2)
        gaussian_window = np.interp(
            gaussian_window, (gaussian_window.min(), gaussian_window.max()), (-1, 1))


#       THREADS
        self.bufferThread = GetBuff(self)
        self.save_thread = SaveThread(self)

        self.measurementThread = ExecuteMeasurementsThread(self)
        self.save_params_thread = SaveParamsThread(self)

        self.VOLmeasurementThread = VolumeScanningThread(self)
        self.referencingThread = GetReferenceThread(self)
        self.systemInitializationThread = InitializationThread(self)
        self.YstageInitializationThread = YstageInitThread(self)
        self.processThread = PostprocessingThread(self)
        self.Yup = YMoveUp(self)
        self.Ydown = YMoveDown(self)
        self.Y_moveto = YMoveTo(self)
        self.Z_moveto = ZMoveTo(self)

        # self.bufferThread.start()

#        BUTTONS SIGNALS
        self.ui.InitBUTTON.clicked.connect(self.set_initparameters)
        self.ui.InitBUTTON.clicked.connect(
            self.systemInitializationThread.start)
        self.ui.InitializeYstageButton.clicked.connect(
            self.YstageInitializationThread.start)
        self.ui.YStageUP.clicked.connect(self.Yup.start)
        self.ui.YStageDOWN.clicked.connect(self.Ydown.start)
        self.ui.Button_YmoveTo.clicked.connect(self.get_startpos)
        self.ui.Button_YmoveTo.clicked.connect(self.Y_moveto.start)
        self.ui.Button_ZmoveTo.clicked.connect(self.get_startpos)
        self.ui.Button_ZmoveTo.clicked.connect(self.Z_moveto.start)

        self.ui.InitBUTTON.clicked.connect(self.set_pyroparameters)
        self.ui.StopButton.clicked.connect(self.stop_measurements)

        self.ui.FolderButton.clicked.connect(self._open_file_dialog)
        self.ui.Measure_button.clicked.connect(self.set_octparameters)
        self.ui.Measure_button.clicked.connect(self.measurementThread.start)

        self.ui.StartCscanBUTTON.clicked.connect(self.set_octparameters)
        self.ui.StartCscanBUTTON.clicked.connect(
            self.set_postprocessparameters)
        self.ui.StartCscanBUTTON.clicked.connect(self.set_cscan_parameters)
        self.ui.StartCscanBUTTON.clicked.connect(
            self.VOLmeasurementThread.start)

        self.ui.Measure_button.clicked.connect(self.ui_measurements_started)
        self.ui.ref_BUTTON.clicked.connect(self.referencingThread.start)
        self.ui.PLOT_BUTTON.clicked.connect(self.graph)
        self.ui.APPLY_button.clicked.connect(self.set_pyroparameters)
        self.ui.SET_OCTParams.clicked.connect(self.set_octparameters)
        self.ui.Aver_checkBox.stateChanged.connect(self.set_octparameters)
        self.ui.APPLY_procparams.clicked.connect(
            self.set_postprocessparameters)
        self.ui.ResetRef_button.clicked.connect(self.reset_ref)
        self.ui.SAVE_button.clicked.connect(self.save)
        self.ui.SAVE_button.clicked.connect(self.save_thread.start)

        self.ui.start_acq_BUTTON.clicked.connect(self.resarray)
        self.ui.stop_acq_BUTTON.clicked.connect(self.stoparray)
        self.ui.actionAbout.triggered.connect(self.openWindow)
        self.ui.ApplyPPC.clicked.connect(self.processThread.start)
        self.ui.start_acq_BUTTON.clicked.connect(self.reset_parameters)
        self.ui.actionSave.triggered.connect(self.save_params_thread.start)


#        OTHER SIGNAL-SLOT CONNECTIONS
        self.referencingThread.refprog.connect(self.refprogress)
        self.referencingThread.refdone.connect(self.plotref)
        self.measurementThread.measprog.connect(self.measprogress)
        self.measurementThread.mdat.connect(self.graph)
        self.measurementThread.mdat.connect(self.ui_measurements_done)
        self.processThread.request_parameters.connect(
            self.set_postprocessparameters)

        self.systemInitializationThread.initdone.connect(self.activatemeas)
        self.YstageInitializationThread.initdone.connect(self.activate3Dmeas)

        self.systemInitializationThread.initdone.connect(
            self.bufferThread.start)
        self.systemInitializationThread.init_status.connect(self.addlogline)

        self.YstageInitializationThread.init_status.connect(self.addlogline)

        self.measurementThread.meas_status.connect(self.addlogline)

        self.VOLmeasurementThread.meas_status.connect(self.addlogline)
        self.VOLmeasurementThread.mdat.connect(self.graph)
        self.VOLmeasurementThread.measprog.connect(self.measprogress)

        self.save_thread.status.connect(self.addlogline)

        self.Yup.status.connect(self.addlogline)
        self.Ydown.status.connect(self.addlogline)
        self.Y_moveto.status.connect(self.addlogline)
        self.Z_moveto.status.connect(self.addlogline)

#        PLOTS
        preset = np.rot90(np.load('./logo/preset.npy'))[:, :155]
        self.ui.BscanWidget.show()
        self.ui.BscanWidget.setImage(20 * np.log10(preset + 0.1))
        self.ui.BscanWidget.view.setAspectLocked(ratio=0.45)
        self.ui.BscanWidget.view.setBackgroundColor(None)
        self.ui.raw_signal_plot.addLegend()
        self.ui.raw_signal_plot.setBackground((35, 35, 35))
        self.ui.curve = self.ui.raw_signal_plot.plot(
            decimate(
                np.zeros(px),
                20,
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
                refers,
                20,
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
                20,
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
        self.timer.start(10)

# Buffer timer
# self.timerbuff = QtCore.QTimer()
# self.timerbuff.timeout.connect(self.getvaluebuff)
# self.timerbuff.start(1)

#        RADIOBUTTONS
        self.ui.NIR_radio.toggled.connect(self.NIRmode)
        self.ui.MIR_radio.toggled.connect(self.MIRmode)

        self.variable = 10
        global ipaddress
        ipaddress = self.ui.IP_var.text()

    def stop_measurements(self):
        global measurement_flag
        measurement_flag = 0

    def _open_file_dialog(self):
        global directory
        directory = str(QtWidgets.QFileDialog.getExistingDirectory())
        print(directory)
        self.ui.FolderLine.setText('{}'.format(directory))

    def openWindow(self):
        self.about = QtWidgets.QMainWindow()
        self.uis = Ui_HelpWindow()
        self.uis.setupUi(self.about)
        self.uis.OKCLOSE.clicked.connect(self.closeWindow)
        self.about = qtmodern.windows.ModernWindow(self.about)

        xa = QtGui.QDesktopWidget().screenGeometry().center().x()
        ya = QtGui.QDesktopWidget().screenGeometry().center().y()
        self.about.show()
        self.about.move(
            xa - self.about.geometry().width() / 2,
            ya - self.about.geometry().height() / 2)

    def closeWindow(self):
        print('q')
        self.about.close()

    def update(self):
        #        self.value=np.random.rand(510)
        global buffer_signal
        self.ui.curve.setData(decimate(buffer_signal, 20, axis=0))

#     def getvaluebuff(self):
# #        self.value=np.random.rand(510)
#          wait=1
    def set_cscan_parameters(self):
        global ystep
        global ystartp
        global ystopp

        ystep = float(self.ui.Y_step.text())
        ystartp = float(self.ui.Y_start_pos.text())
        ystopp = float(self.ui.Y_stop_pos.text())

    def activatemeas(self):
        self.ui.Measure_button.setEnabled(True)
        self.ui.SAVE_button.setEnabled(True)
        self.ui.ref_BUTTON.setEnabled(True)
        self.ui.Button_ZmoveTo.setEnabled(True)

    def activate3Dmeas(self):
        self.ui.StartCscanBUTTON.setEnabled(True)
        self.ui.YStageUP.setEnabled(True)
        self.ui.YStageDOWN.setEnabled(True)
        self.ui.Button_YmoveTo.setEnabled(True)

    def reset_ref(self):
        global refers
        refers = np.zeros(px)
        self.ui.refcurve.setData(refers)

    def measprogress(self, pbar):
        self.ui.scanprogressBar.setValue(int(pbar))

    @Slot(object)
    def addlogline(self, status_text):
        self.ui.logbrowser.append(status_text)

    def save(self):
        global filename
        global logcoeff
        filename = self.ui.filenameline.text()
        logcoeff = float(self.ui.inlog_coef.text())

    def refprogress(self, rpbar):
        self.ui.refprogressBar.setValue(int(rpbar))

    def plotref(self):
        global refers
        self.ui.refcurve.setData(decimate(refers, 20, axis=0))

    def graph(self):
        self.ui.BscanWidget.setImage(
            20 *
            np.log10(
                np.rot90(scan) +
                float(
                    self.ui.inlog_coef.text())))
        self.ui.BscanWidget.view.setAspectLocked(
            ratio=float(self.ui.aspectr.text()))
        self.ui.logbrowser.append('Data visualized successfully')

    def set_pyroparameters(self):
        global sfreq
        global vdr
        global vvr
        global delay
        global pulw
        global ipaddress
        ipaddress = self.ui.IP_var.text()
        print(ipaddress)

    def set_initparameters(self):
        # READ OUT GUI PARAMS TO SET THEM
        global rangmin
        global rangmax
        global delay
        # Part of buff <PX>
        rangmin = int(self.ui.rang_start.text())
        rangmax = int(self.ui.rang_stop.text())
        delay = str(self.ui.delay_var.text())

    def reset_parameters(self):
        # READ OUT GUI PARAMS TO SET THEM
        global rangmin
        global rangmax
        global px
        global refern
        global scanrange
        global refern
        global data
        global output
        global outputfft
        global delay

        # Part of buff <PX>
        rangmin = int(self.ui.rang_start.text())
        rangmax = int(self.ui.rang_stop.text())
        px = rangmax - rangmin
        scanrange = np.flip(np.arange(stopp, startp + step, step), 0)
        refern = np.zeros([refnum, px])
        # spectarr = (c_float*510)()
        data = np.zeros([px, num])
        output = np.zeros([px, len(scanrange)])
        outputfft = np.zeros([px, len(scanrange)])
        gaussian_window = np.exp(-1 / 2 * ((np.linspace(-(px - 1) / 2,
                                 (px - 1) / 2, px) - posw) / (4 * gaw))**2)
        gaussian_window = np.interp(
            gaussian_window, (gaussian_window.min(), gaussian_window.max()), (-1, 1))
        self.ui.gaussian.setData(decimate(gaussian_window, 20, axis=0))
        delay = str(self.ui.delay_var.text())
        rp_s.tx_txt('ACQ:TRIG:DLY ' + delay)

    def get_startpos(self):
        global ystartp
        ystartp = float(self.ui.Y_start_pos.text())
        global startp
        startp = float(self.ui.instarttp.text())

    def set_octparameters(self):
        global num
        global refnum
        global step
        global startp
        global stopp
        global idle_time
        global data
        global refern
        global scanrange
        global outputfft
        global output
        global gaw
        global posw
        global ystep
        global ystartp
        global ystopp

        if self.ui.Aver_checkBox.isChecked():
            print('Averaging mode')
            num = int(self.ui.innum.text())  # Number of averaged pixels
        else:
            print('No averaging')
            num = 1  # Number of averaged pixels

        refnum = int(self.ui.inrefnum.text())
        step = float(self.ui.instep.text())
        startp = float(self.ui.instarttp.text())
        stopp = float(self.ui.instopp.text())

        ystep = float(self.ui.Y_step.text())
        ystartp = float(self.ui.Y_start_pos.text())
        ystopp = float(self.ui.Y_stop_pos.text())

        idle_time = float(self.ui.intid.text())

        data = np.zeros([px, num])
        refern = np.zeros([refnum, px])
        scanrange = np.flip(np.arange(stopp, startp + step, step), 0)

        output = np.zeros([px, len(scanrange)])
        outputfft = np.zeros([px, len(scanrange)])

    def set_postprocessparameters(self):

        global wave_left
        global wh
        global gaw
        global posw
        wave_left = int(self.ui.inwl.text())
        wh = int(self.ui.inwh.text())
        gaw = int(self.ui.ingw.text())
        posw = int(self.ui.ina.text())
        self.ui.logbrowser.append(
            '\nBandwidth SET, LOW Wavelength: ' + str(wave_left))
        self.ui.logbrowser.append('Bandwidth SET, HIGH Wavelength: ' + str(wh))
        self.ui.logbrowser.append('Gaussian window width (STD): ' + str(gaw))
        self.ui.logbrowser.append(
            'Gaussian window position: ' + str(posw) + '\n')

        gaussian_window = np.exp(-1 / 2 * ((np.linspace(-(px - 1) / 2,
                                 (px - 1) / 2, px) - posw) / (4 * gaw))**2)
        gaussian_window = np.interp(
            gaussian_window, (gaussian_window.min(), gaussian_window.max()), (-1, 1))
        self.ui.gaussian.setData(decimate(gaussian_window, 20, axis=0))

    def NIRmode(self):
        global wave_left
        global wh
        global gaw
        global posw
        wave_left = 1850
        wh = 2150
        gaw = 200
        posw = 0
        self.ui.inwh.setText(str(wh))
        self.ui.inwl.setText(str(wave_left))
        self.ui.ingw.setText(str(gaw))
        self.ui.aspectr.setText('1')
        gaussian_window = np.exp(-1 / 2 * ((np.linspace(-(px - 1) / 2,
                                 (px - 1) / 2, px) - posw) / (4 * gaw))**2)
        gaussian_window = np.interp(
            gaussian_window, (gaussian_window.min(), gaussian_window.max()), (-1, 1))
        self.ui.gaussian.setData(decimate(gaussian_window, 20, axis=0))

    def MIRmode(self):
        global wave_left
        global wh
        global gaw
        global posw
        wave_left = 3720
        wh = 4200
        gaw = 50
        posw = -60
        self.ui.inwh.setText(str(wh))
        self.ui.inwl.setText(str(wave_left))
        self.ui.ingw.setText(str(gaw))
        self.ui.ina.setText(str(posw))
        self.ui.aspectr.setText('0.5')
        gaussian_window = np.exp(-1 / 2 * ((np.linspace(-(px - 1) / 2,
                                 (px - 1) / 2, px) - posw) / (4 * gaw))**2)
        gaussian_window = np.interp(
            gaussian_window, (gaussian_window.min(), gaussian_window.max()), (-1, 1))
        self.ui.gaussian.setData(decimate(gaussian_window, 20, axis=0))
        self.variable = 20

    def stoparray(self):
        print('Stopped')

    def resarray(self):
        self.ui.logbrowser.append('Parameters set')

    def ui_measurements_started(self):
        self.ui.InitBUTTON.setEnabled(False)
        self.ui.SET_OCTParams.setEnabled(False)
        self.ui.ApplyPPC.setEnabled(False)

    def ui_measurements_done(self):
        self.ui.InitBUTTON.setEnabled(True)
        self.ui.SET_OCTParams.setEnabled(True)
        self.ui.ApplyPPC.setEnabled(True)

    def closeEvent(self, event):
        global flag

        flag = 1
        # self.ui.BscanWidget.deleteLater()
        # self.ui.curve.deleteLater()
        time.sleep(1)
        self.ui.BscanWidget.setParent(None)
        print('Close')
        QApplication.quit()


"""
THREADS
"""


class GetReferenceThread(QtCore.QThread):

    refprog = QtCore.Signal(object)
    refdone = QtCore.Signal(object)

    def __init__(self, parent=win):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        # shutt.write(('close_shutt').encode('utf-8'))
        # time.sleep(4)
        for i in range(0, len(refern)):
            time.sleep(idle_time)
            global buffer_signal
            rvalue = buffer_signal
            refern[i, :] = rvalue

#                self.parent().ui.refprogressBar.setValue((i+1)/len(refern)*100)
            self.refprogress = (i + 1) / len(refern) * 100
            self.refprog.emit(self.refprogress)

        # shutt.write(('init_pos').encode('utf-8'))
        time.sleep(4)

        global refers
        refers = np.mean(refern, 0)
        self.refdone.emit(self.refprogress)


class YMoveUp(QtCore.QThread):
    status = QtCore.Signal(object)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        global motor
        motor.move_by(-0.5, True)
        print('Moved up by 0.5 mm')
        self.msg = 'Moved up by 0.5 mm'
        self.status.emit(self.msg)


class YMoveDown(QtCore.QThread):
    status = QtCore.Signal(object)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        global motor
        motor.move_by(0.5, True)
        print('Moved down by 0.5 mm')
        self.msg = 'Moved down by 0.5 mm'
        self.status.emit(self.msg)


class YMoveTo(QtCore.QThread):
    status = QtCore.Signal(object)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        global motor
        global ystartp
        motor.move_to(ystartp, True)
        self.msg = 'Moved to start Y position'
        self.status.emit(self.msg)


class ZMoveTo(QtCore.QThread):
    status = QtCore.Signal(object)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        global motor
        global startp
        pidevice.MOV(pidevice.axes, startp)
        self.msg = 'Moved to start X position'
        self.status.emit(self.msg)


class VolumeScanningThread(QtCore.QThread):
    measprog = QtCore.Signal(object)
    mdat = QtCore.Signal(object)
    meas_status = QtCore.Signal(object)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        start_time = time.time()
        global scan
        global scanf
        global scans
        global flag
        global measurement_flag

        global ystep
        global ystartp
        global ystopp

        global buffer_signal
        global num
        global refnum
        global step
        global startp
        global stopp
        global idle_time
        global data
        global refern
        global scanrange
        global outputfft
        global output
        global gaw
        global posw
        global wave_left
        global wh
        global buffer_signal
        global scan
        global flag
        global measurement_flag

        yscanrange = np.flip(np.arange(ystopp, ystartp + ystep, ystep), 0)

        ascanav = np.zeros([px, num, len(scanrange)])

        vscan = np.zeros([len(yscanrange), 512, len(scanrange)])

        totalmeasurements = len(yscanrange) * len(scanrange)

        # START MEASUREMENT
        start_time = time.time()
        len_counter = 1
        z_counter = 1

        for zpos in range(0, len(yscanrange)):

            print(yscanrange[zpos])
            print(zpos)

            motor.move_to(yscanrange[zpos], True)

            if measurement_flag == 0:
                measurement_flag = 1
                break

            for itn in range(0, len(scanrange)):
                print('Position:', round(scanrange[itn], 3), 'mm')
                if measurement_flag == 0:
                    break

                for i in range(0, num):
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
                    data[:, i] = np.flip(buffer_signal, 0)
                    # FOR FUTHER FFT AVERAGING
                    ascanav[:, i, itn] = np.flip(buffer_signal, 0)
                    time.sleep(idle_time)
                    if flag != 0:
                        break
                output[:, itn] = np.mean(data, 1)
                avft = np.flip(np.rot90(data, 1), 1)
                outputfft[:, itn] = np.mean(scanProcess(np.flip(remap_to_k(
                    avft, refers, wave_left, wh, cal_vector, boundaries), 0), typ='n', px=px, a=posw, Std=gaw), 0)

                len_counter = len_counter + 1

                self.progress = 100 * \
                    (len_counter + z_counter) / totalmeasurements
                self.measprog.emit(self.progress)
                if flag != 0:
                    break
            topost = np.flip(np.rot90(output, 1), 1)
            if flag != 0:
                break

            # PROCESS
            scan = scanProcess(
                np.flip(
                    remap_to_k(
                        topost,
                        refers,
                        wave_left,
                        wh,
                        cal_vector,
                        boundaries),
                    0),
                typ='n',
                px=px,
                a=posw,
                Std=gaw)
            scanf = np.rot90(scan)

            vscan[zpos, :, :] = scanf[int(px / 2):int(px / 2) + 512, :]
            scans = vscan
            scan = np.flip(np.moveaxis(
                np.flip(vscan[:zpos + 1, :, :], 0), -1, 0), 1)
            z_counter = z_counter + 1
            if np.shape(scan)[1] > 0:
                self.mdat.emit(self.progress)
                print(np.shape(scan))

        motor.move_to(yscanrange[0])

        global vscancheck
        vscancheck = vscan
        # scan=vscan
        scan = np.moveaxis(np.flip(vscan, 0), -1, 0)
        print('3D measurement completed')
        self.ms_msg = '3D scan DONE in ' + \
            "--- %s seconds ---" % (time.time() - start_time)
        self.meas_status.emit(self.ms_msg)
        self.progress = 100
        self.measprog.emit(self.progress)


class ExecuteMeasurementsThread(QtCore.QThread):
    measprog = QtCore.Signal(object)
    mdat = QtCore.Signal(object)
    meas_status = QtCore.Signal(object)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        err = 0
        start_time = time.time()
        global outputfft
        global scan
        global scanf
        global scans
        global flag
        global measurement_flag

        if len(data) == len(refers):
            self.ms_msg = 'Measurements started...\n' + 'Scan length: ' + \
                str(startp - stopp) + 'mm\n' + 'Averaging: ' + str(num)
            self.meas_status.emit(self.ms_msg)
            for itn in range(0, len(scanrange)):
                print(
                    'Position: ',
                    round(
                        scanrange[itn],
                        2),
                    'mm; Errors: ',
                    err,
                    '; Av.num:',
                    num,
                    ';  Gaussian window:',
                    gaw,
                    ' WinWidth: ',
                    posw)
    #            position=round(scanrange[itn],3)
                self.progress = 100 * (itn + 1) / len(scanrange)
                self.measprog.emit(self.progress)

                if measurement_flag == 0:
                    measurement_flag = 1
                    break
                for i in range(0, num):
                    if flag != 0:
                        break
                    time.sleep(idle_time)
                    global buffer_signal
                    data[:, i] = np.flip(buffer_signal, 0)
            #                data[:,i] = sosfiltfilt(soss, data[:,i])

                output[:, itn] = np.mean(data, 1)

                avft = np.flip(np.rot90(data, 1), 1)
                outputfft[:, itn] = np.mean(scanProcess(np.flip(remap_to_k(
                    avft, refers, wave_left, wh, cal_vector, boundaries), 0), typ='n', px=px, a=posw, Std=gaw), 0)
                if flag != 0:
                    break
            topost = np.flip(np.rot90(output, 1), 1)
            global rawdat
            rawdat = np.copy(topost)

            # PROCESS
            scan = scanProcess(
                np.flip(
                    remap_to_k(
                        topost,
                        refers,
                        wave_left,
                        wh,
                        cal_vector,
                        boundaries),
                    0),
                typ='n',
                px=px,
                a=posw,
                Std=gaw)
            scanf = np.rot90(scan)

            # AVERAGE WITH MEAN FOURIER SPACE
            cuscus = np.average([norma(scanf[int(px /
                                                 2):int(px /
                                                        2 +
                                                        512), :], norma=0), norma(outputfft[int(px /
                                                                                                2 +
                                                                                                1):int(px /
                                                                                                       2 +
                                                                                                       512 +
                                                                                                       1), :], norma=0)], 0)
            cuscus = norma(cuscus, norma=0)

    #        scan=cuscus[:-100,:]
            purescn = norma(scanf, norma=0)
            pureftscn = norma(outputfft, norma=0)

            global scans
            scans = np.array([cuscus, purescn[int(px /
                                                  2):int(px /
                                                         2 +
                                                         512), :], pureftscn[int(px /
                                                                                 2 +
                                                                                 1):int(px /
                                                                                        2 +
                                                                                        512 +
                                                                                        1), :]])

            # scans=np.array([cuscus[int(px/2):int(px/2+800),:],purescn[int(px/2):int(px/2+800),:],pureftscn[int(px/2):int(px/2+800),:]])
            scan = np.moveaxis(np.flip(scans, 0), -1, 0)
            print("--- %s seconds ---" % (time.time() - start_time))
            # np.save('topost.npy', topost)
            self.ms_msg = 'DONE in ' + \
                "--- %s seconds ---" % (time.time() - start_time)
            self.meas_status.emit(self.ms_msg)
            self.mdat.emit(self.progress)
        else:
            self.ms_msg = 'ERROR - Referencing is needed'
            self.meas_status.emit(self.ms_msg)


class PostprocessingThread(QtCore.QThread):
    request_parameters = QtCore.Signal(object)

    def __init__(self, parent=win):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        self.request_parameters.emit(self)
        print(wave_left)
        print(wh)
        print(gaw)
        print(posw)
        # PROCESS
#        local_outputfft=raw_fftout
        global rawdat
        local_topost = np.copy(rawdat)
        local_scan = scanProcess(
            np.flip(
                remap_to_k(
                    local_topost,
                    refers,
                    wave_left,
                    wh,
                    cal_vector,
                    boundaries),
                0),
            typ='n',
            px=px,
            a=posw,
            Std=gaw)
        local_scanf = np.rot90(local_scan)
        # AVERAGE WITH MEAN FOURIER SPACE
#        local_cuscus=np.average([norma(local_scanf[256:-1,:],norma=0),norma(local_outputfft[257:,:],norma=0)],0)
#        local_cuscus=norma(local_cuscus,norma=0)
        local_purescn = local_scanf[int(px / 2):int(px / 2 + 512), :]
#        local_pureftscn=norma(local_outputfft[257:,:],norma=0)
#        local_scans=np.array([local_cuscus[:-100,:],local_purescn[:-100,:],local_pureftscn[:-100,:]])
        global scan
        scan = np.flip(local_purescn, 1)
        del local_topost


class YstageInitThread(QtCore.QThread):
    initdone = QtCore.Signal(object)
    init_status = QtCore.Signal(object)

    def __init__(self, parent=win):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        global motor
        # Y STAGE INITIALIZATION
        try:
            print('Y stage initialization')
            print(motor.get_velocity_parameters())
            motor.set_velocity_parameters(2.4, 5, 2.4)

            motor.move_home(True)
            motor.move_to(15, True)
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

    def __init__(self, parent=win):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        global shutt
        global pidevice
        global rp_s
        global rangmin
        global rangmax
        global px
        global scanrange
        global refern
        global data
        global output
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
        px = rangmax - rangmin

        stagesn = '0115500223'
        # stagesn='020550328'

        b, a = scisig.butter(4, 0.0005, btype='highpass')

        # GLOBAL EMPTHY VARIABLES
        scanrange = np.flip(np.arange(stopp, startp + step, step), 0)
        refern = np.zeros([refnum, px])
        position = 0
        # spectarr = (c_float*510)()
        data = np.zeros([px, num])
        output = np.zeros([px, len(scanrange)])
        outputfft = np.zeros([px, len(scanrange)])

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


class SaveThread(QtCore.QThread):
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
                        self.msg = 'Tif volume saved in ' + './output/'
                        self.status.emit(self.msg)
                        tif.imwrite(
                            './output/' +
                            filename +
                            datetime.now().strftime('%Y-%m-%d_%H-%M') +
                            '.tif',
                            scans_to_save,
                            photometric='minisblack')
            except BaseException:
                np.save(
                    './output/' +
                    filename +
                    datetime.now().strftime('%Y-%m-%d_%H-%M') +
                    '.npy',
                    scans)
                self.msg = 'Saved in ' + './output/'
                self.status.emit(self.msg)
                if np.shape(scans)[0] > 3:
                    scans_to_save = 20 * np.log10(np.copy(scans) + logcoeff)
                    scans_to_save = scans_to_save - np.min(scans_to_save)
                    scans_to_save = scans_to_save / \
                        np.max(scans_to_save) * 65536
                    scans_to_save = scans_to_save[:, :, :]
                    scans_to_save = scans_to_save.astype(np.uint16)
                    self.msg = 'Tif volume saved in ' + './output/'
                    self.status.emit(self.msg)
                    tif.imwrite(
                        './output/' +
                        filename +
                        datetime.now().strftime('%Y-%m-%d_%H-%M') +
                        '.tif',
                        scans_to_save,
                        photometric='minisblack')
                # self.ui.logbrowser.append('Saved as: '+('./output/'+filename+datetime.now().strftime('%Y-%m-%d_%H-%M')+'.npy \n'))
        else:
            print('Empthy data')
            # self.ui.logbrowser.append('Scan cannot be saved, EmptyData')


class GetBuff(QtCore.QThread):

    def __init__(self, parent=win):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        global flag, buffer_signal
        self.active = True
        while flag == 0:
            buffer_signal = np.random.rand(16384)


class SaveParamsThread(QtCore.QThread):
    status = QtCore.Signal(object)

    def __init__(self, parent=win):
        QtCore.QThread.__init__(self, parent)

    def run(self):

        global wave_left
        global wh
        global gaw
        global refers
        global num
        global refnum
        global step
        global startp
        global stopp
        global idle_time
        global data
        global px
        global scan
        global posw
        global buffer_signal
        global output
        global gaussian_window
        global rawdat
        global flag
        global rp_s
        global motor
        global directory
        global measurement_flag
        global ystep
        global ystartp
        global ystopp

        np.save('./reference/ref.npy', refers)


if __name__ == "__main__":
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QtCore.QCoreApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    qtmodern.styles.dark(app)
    mwins = win()
    mwins = qtmodern.windows.ModernWindow(mwins)
    mwins.show()
    sys.exit(app.exec_())
