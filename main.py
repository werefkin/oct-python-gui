import sys
from modules.shared_vars import SharedVariables
from modules.get_buffer_thread import GetBufferThread
from modules.octlib import OCTLib
from modules.proc_ui import Ui_MainWindow
from modules.help_ui import Ui_HelpWindow
from modules.vol_ui import Ui_VolumetricWidget
from datetime import datetime
import time
import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import Slot
import qtmodern.styles
import qtmodern.windows
from scipy.signal import decimate
import tifffile as tif
import os
import logging
import pyqtgraph.opengl

if os.name == 'nt':
    from ctypes import windll  # Change the timer resolution of Windows
    # Change the timer resolution of Windows to 1 ms
    timeBeginPeriod = windll.winmm.timeBeginPeriod
    timeBeginPeriod(1)  # Change the timer resolution of Windows

logging.basicConfig(level=logging.INFO, format='%(message)s')


class win(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Init variables
        self.shared_vars = SharedVariables()
        self.shared_vars.load_parameters()
        self.set_saved_parameters()

#       THREADS
        self.buffer_thread = GetBufferThread(self.shared_vars)
        self.save_thread = SaveDataThread(self.shared_vars)
        self.bscan_measurement_thread = BScanMeasureThread(self.shared_vars)
        self.cscan_measurement_thread = VolumeScanningThread(self.shared_vars)
        self.save_params_thread = SaveParamsThread(self.shared_vars)
        self.referencing_thread = GetReferenceThread(self.shared_vars)
        self.sys_init_thread = InitializationThread(
            self.shared_vars, self.buffer_thread)
        self.ystage_init_thread = YstageInitThread(self)
        self.post_process_thread = PostProcessingThread(self.shared_vars)
        self.y_stage_up = YMoveUpByThread(self.shared_vars)
        self.y_stage_down = YMoveDownByThread(self.shared_vars)
        self.y_axis_move_to = YPositionToThread(self.shared_vars)
        self.x_axis_move_to = XPositionToThread(self.shared_vars)

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

        # self.continuous_button.clicked.connect(self.run_continuous)
        # self.Bscan_MeasureButton.clicked.connect(self.run_one_time)

        self.ui.InitButton.clicked.connect(self.set_acq_parameters)
        self.ui.StopButton.clicked.connect(self.stop_measurements)

        self.ui.FolderButton.clicked.connect(self._open_file_dialog)
        self.ui.Bscan_MeasureButton.clicked.connect(self.set_octparameters)
        self.ui.Bscan_MeasureButton.clicked.connect(
            self.bscan_measurement_thread.start)

        self.ui.StartCscanButton.clicked.connect(self.set_octparameters)
        self.ui.StartCscanButton.clicked.connect(
            self.set_postprocessparameters)
        self.ui.StartCscanButton.clicked.connect(self.set_cscan_parameters)
        self.ui.StartCscanButton.clicked.connect(
            self.cscan_measurement_thread.start)

        self.ui.Bscan_MeasureButton.clicked.connect(
            self.status_ui_measurements_started)
        self.ui.ReferenceButton.clicked.connect(self.set_octparameters)
        self.ui.ReferenceButton.clicked.connect(self.referencing_thread.start)
        self.ui.PlotButton.clicked.connect(self.graph)
        self.ui.ApplyButton.clicked.connect(self.set_acq_parameters)
        self.ui.SetOCTParamsButton.clicked.connect(self.set_octparameters)
        self.ui.AveragingCheckBox.stateChanged.connect(self.set_octparameters)
        self.ui.ContinousBscancheckBox.stateChanged.connect(self.nonstop_bscan)

        self.ui.SetProcParamsButton.clicked.connect(
            self.set_postprocessparameters)
        self.ui.ResetReferenceButton.clicked.connect(self.reset_ref)
        self.ui.SaveButton.clicked.connect(self.save)
        self.ui.SaveButton.clicked.connect(self.save_thread.start)

        self.ui.SetRangeButton.clicked.connect(self.reset_parameters)
        self.ui.SetRangeButton.clicked.connect(self.resarray)
        self.ui.SetRangeButton.clicked.connect(self.buffer_thread.start)
        self.ui.StopAcqButton.clicked.connect(self.stop_spectrometer)
        self.ui.actionAbout.triggered.connect(self.openWindow)
        self.ui.actionVolumetric_plotter.triggered.connect(self.run_volumetric)

        self.ui.ApplyProcButton.clicked.connect(
            self.set_postprocessparameters)

        self.ui.ApplyProcButton.clicked.connect(self.post_process_thread.start)
        self.ui.actionSave.triggered.connect(self.set_parameters_to_save)
        self.ui.actionSave.triggered.connect(self.save_params_thread.start)

        # VALIDATORS
        self.ui.a_idle_time.setValidator(QtGui.QDoubleValidator(0.00000, 10000.000, 5, notation=QtGui.QDoubleValidator.StandardNotation))
        self.ui.avg_num_ui.setValidator(QtGui.QIntValidator(1, 10000))
        self.ui.wave_right_ui.setValidator(QtGui.QDoubleValidator(0, 100000.00, 3, notation=QtGui.QDoubleValidator.StandardNotation))
        self.ui.wave_left_ui.setValidator(QtGui.QDoubleValidator(0, 100000.00, 3, notation=QtGui.QDoubleValidator.StandardNotation))
        self.ui.gaussian_std_ui.setValidator(QtGui.QDoubleValidator(1, 100000.00, 3, notation=QtGui.QDoubleValidator.StandardNotation))
        self.ui.gaussian_pos_ui.setValidator(QtGui.QDoubleValidator(0, 100000.00, 3, notation=QtGui.QDoubleValidator.StandardNotation))
        self.ui.sampling_start_ui.setValidator(QtGui.QIntValidator(0, 100000))
        self.ui.sampling_stop_ui.setValidator(QtGui.QIntValidator(1, 100000))
        self.ui.x_start_pos_ui.setValidator(QtGui.QDoubleValidator(0, 100000.00, 3, notation=QtGui.QDoubleValidator.StandardNotation))
        self.ui.x_stop_pos_ui.setValidator(QtGui.QDoubleValidator(0, 100000.00, 3, notation=QtGui.QDoubleValidator.StandardNotation))
        self.ui.x_step_ui.setValidator(QtGui.QDoubleValidator(0, 100000.00, 3, notation=QtGui.QDoubleValidator.StandardNotation))
        self.ui.ui_y_start_pos.setValidator(QtGui.QDoubleValidator(0, 100000.00, 3, notation=QtGui.QDoubleValidator.StandardNotation))
        self.ui.ui_y_stop_pos.setValidator(QtGui.QDoubleValidator(0, 100000.00, 3, notation=QtGui.QDoubleValidator.StandardNotation))
        self.ui.y_step.setValidator(QtGui.QDoubleValidator(0, 100000.00, 3, notation=QtGui.QDoubleValidator.StandardNotation))
        self.ui.aspect_ratio.setValidator(QtGui.QDoubleValidator(0, 10.00, 3, notation=QtGui.QDoubleValidator.StandardNotation))
        self.ui.log10_coef.setValidator(QtGui.QDoubleValidator(0, 1000000000.00, 3, notation=QtGui.QDoubleValidator.StandardNotation))


#        OTHER SIGNAL-SLOT CONNECTIONS
        self.referencing_thread.refprog.connect(self.refprogress)
        self.referencing_thread.refdone.connect(self.plotref)
        self.bscan_measurement_thread.measprog.connect(self.measprogress)
        self.bscan_measurement_thread.mdat.connect(self.graph)
        self.bscan_measurement_thread.mdat.connect(
            self.status_ui_measurements_done)
        self.post_process_thread.request_parameters.connect(
            self.set_postprocessparameters)

        self.sys_init_thread.initdone.connect(self.activatemeas)
        self.sys_init_thread.initdone.connect(self.set_saved_parameters)
        self.ystage_init_thread.initdone.connect(self.activate3Dmeas)
        self.sys_init_thread.initdone.connect(self.reset_parameters)

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
        self.ui.BscanWidget.show()
        self.ui.BscanWidget.setImage(
            20 *
            np.log10(
                np.rot90(
                    self.shared_vars.b_scan) +
                0.1))
        self.ui.BscanWidget.view.setAspectLocked(ratio=0.45)
        self.ui.BscanWidget.view.setBackgroundColor(None)
        self.ui.raw_signal_plot.addLegend()
        self.ui.raw_signal_plot.setBackground((35, 35, 35))
        self.ui.curve = self.ui.raw_signal_plot.plot(
            decimate(
                np.zeros(self.shared_vars.samples_num),
                self.shared_vars.decimation_factor,
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
                self.shared_vars.reference_spectrum,
                self.shared_vars.decimation_factor,
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
                self.shared_vars.gaussian_window,
                self.shared_vars.decimation_factor,
                axis=0),
            pen={
                'color': (
                    252,
                    142,
                    51),
                'width': 2},
            name='Gaussian window')
        self.ui.raw_signal_plot.setYRange(0, 3)
        # self.ui.raw_signal_plot.setXRange(0,800)
        self.ui.raw_signal_plot.setClipToView(True)


#        TIMER AND LIVE SIGNAL UPD
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100)

#        RADIOBUTTONS
        self.ui.Preset2Radio.toggled.connect(self.preset2_mode)
        self.ui.Preset1Radio.toggled.connect(self.preset1_mode)

    # METHODS OF MAIN

    def stop_measurements(self):
        self.shared_vars.measurement_flag = 0
        self.shared_vars.inloop_flag = 0

    def nonstop_bscan(self):
        if self.ui.ContinousBscancheckBox.isChecked():
            self.shared_vars.run_continuous = True
        else:
            self.shared_vars.run_continuous = False

    def _open_file_dialog(self):
        self.shared_vars.directory = str(
            QtWidgets.QFileDialog.getExistingDirectory())
        print(self.shared_vars.directory)
        self.ui.FolderLine.setText('{}'.format(self.shared_vars.directory))

    def openWindow(self):
        self.about = QtWidgets.QMainWindow()
        self.uis = Ui_HelpWindow()
        self.uis.setupUi(self.about)
        self.uis.OKCloseButton.clicked.connect(self.closeWindow)
        self.about = qtmodern.windows.ModernWindow(self.about)
        qr = self.about.frameGeometry()
        cp = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.about.move(qr.topLeft())
        self.about.show()

    def run_volumetric(self):
        self.volumetric = QtWidgets.QMainWindow()
        self.voluis = Ui_VolumetricWidget()
        self.voluis.setupUi(self.volumetric)
        self.voluis.ApplyRenderingButton.clicked.connect(self.plot_upd_volume)
        self.voluis.SetAnglesButton.clicked.connect(self.set_angles_volume)
        qr = self.volumetric.frameGeometry()
        cp = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.volumetric.move(qr.topLeft())
        self.volumetric.show()
        self.data_4d = None
        # create a 3D array
        self.plot_volume()
        # self.vol_plotter_thread = some_thread() # if some thread is needed
        # self.vol_plotter_thread.start()

    def plot_volume(self):
        if self.shared_vars.scans is None:
            self.shared_vars.scans = np.load('./logo/cscan.npy')
        self.volume = 20 * np.log10(self.shared_vars.scans + 2)

        if self.data_4d is None:
            self.volume = (self.volume - np.min(self.volume)) / (np.max(self.volume) - np.min(self.volume))
            self.data_4d = np.array([4 * 1024 * self.volume, 4 * 1024 * self.volume, 4 * 1024 * self.volume, 4 * 512 * self.volume])
            self.data_4d = np.transpose(self.data_4d, (1, 2, 3, 0))
            # create a GLVolumeItem and add it to the view
            vol = pyqtgraph.opengl.GLVolumeItem(self.data_4d)
            self.voluis.CscanWidget.addItem(vol)
            self.voluis.CscanWidget.setCameraPosition(distance=1000)
            self.voluis.CscanWidget.show()

    def plot_upd_volume(self):
        self.volume = 20 * np.log10(self.shared_vars.scans + float(self.voluis.log10_coef_3d_ui.text()))
        self.volume = (self.volume - np.min(self.volume)) / (np.max(self.volume) - np.min(self.volume))
        self.data_4d = np.array([4 * 1024 * self.volume, 4 * 1024 * self.volume, 4 * 1024 * self.volume, 4 * 512 * self.volume])
        self.data_4d = np.transpose(self.data_4d, (1, 2, 3, 0))
        # create a GLVolumeItem and add it to the view
        vol = pyqtgraph.opengl.GLVolumeItem(self.data_4d)
        self.voluis.CscanWidget.clear()
        self.voluis.CscanWidget.addItem(vol)
        self.voluis.CscanWidget.setCameraPosition(distance=1000)
        self.voluis.CscanWidget.show()
        camera_params = self.voluis.CscanWidget.cameraParams()
        print("Camera parameters: ", camera_params)

    def set_angles_volume(self):
        self.voluis.CscanWidget.setCameraPosition(azimuth=float(self.voluis.x_angle_ui.text()), elevation=float(self.voluis.y_angle_ui.text()), distance=float(self.voluis.distance_ui.text()))
        camera_params = self.voluis.CscanWidget.cameraParams()
        print("Cew camera parameters: ", camera_params)

    def closeWindow(self):
        print('q')
        self.about.close()

    def update(self):
        #        self.value=np.random.rand(510)
        self.ui.curve.setData(
            decimate(
                self.shared_vars.buffer_signal,
                self.shared_vars.decimation_factor,
                axis=0))

    def set_cscan_parameters(self):

        self.shared_vars.ystep = float(self.ui.y_step.text())
        self.shared_vars.ystart_coordinate = float(
            self.ui.ui_y_start_pos.text())
        self.shared_vars.ystop_coordinate = float(self.ui.ui_y_stop_pos.text())

    def activatemeas(self):
        self.ui.Bscan_MeasureButton.setEnabled(True)
        self.ui.SaveButton.setEnabled(True)
        self.ui.ReferenceButton.setEnabled(True)
        self.ui.Button_XMoveTo.setEnabled(True)

    def set_saved_parameters(self):
        self.ui.a_idle_time.setText(str(self.shared_vars.idle_time))
        self.ui.sampling_start_ui.setText(str(self.shared_vars.sample_min))
        self.ui.sampling_stop_ui.setText(str(self.shared_vars.sample_max))
        self.ui.trig_delay.setText(str(self.shared_vars.sig_delay))
        self.ui.FolderLine.setText(str(self.shared_vars.directory))
        self.ui.filenameline.setText(str(self.shared_vars.filename))
        self.ui.log10_coef.setText(str(self.shared_vars.log_coeff))
        self.ui.param1.setText(str(self.shared_vars.param1))
        self.ui.avg_num_ui.setText(str(self.shared_vars.avg_num))
        self.ui.wave_right_ui.setText(str(self.shared_vars.wave_right))
        self.ui.wave_left_ui.setText(str(self.shared_vars.wave_left))
        self.ui.ref_avg_num_ui.setText(str(self.shared_vars.ref_avg_num))
        self.ui.x_stop_pos_ui.setText(str(self.shared_vars.xstop_coordinate))
        self.ui.x_start_pos_ui.setText(str(self.shared_vars.xstart_coordinate))
        self.ui.x_step_ui.setText(str(self.shared_vars.x_step))
        self.ui.ui_y_start_pos.setText(str(self.shared_vars.ystart_coordinate))
        self.ui.ui_y_stop_pos.setText(str(self.shared_vars.ystop_coordinate))
        self.ui.y_step.setText(str(self.shared_vars.ystep))
        self.ui.gaussian_std_ui.setText(str(self.shared_vars.gaussian_std_ui))
        self.ui.gaussian_pos_ui.setText(str(self.shared_vars.gaussian_pos))
        self.ui.aspect_ratio.setText(str(self.shared_vars.aspect_ratio))

    def activate3Dmeas(self):
        self.ui.StartCscanButton.setEnabled(True)
        self.ui.YStageUpButton.setEnabled(True)
        self.ui.YStageDownButton.setEnabled(True)
        self.ui.YStageMoveToButton.setEnabled(True)

    def reset_ref(self):
        self.shared_vars.reference_spectrum = np.zeros(
            self.shared_vars.samples_num)
        self.ui.refcurve.setData(
            decimate(
                self.shared_vars.reference_spectrum,
                self.shared_vars.decimation_factor,
                axis=0))

    def measprogress(self, pbar):
        self.ui.scanprogressBar.setValue(int(pbar))

    @Slot(object)
    def addlogline(self, status_text):
        self.ui.logbrowser.append(status_text)

    def save(self):
        self.shared_vars.filename = self.ui.filenameline.text()
        self.shared_vars.log_coeff = float(self.ui.log10_coef.text())

    def refprogress(self, rpbar):
        self.ui.refprogressBar.setValue(int(rpbar))

    def plotref(self):
        self.ui.refcurve.setData(
            decimate(
                self.shared_vars.reference_spectrum,
                self.shared_vars.decimation_factor,
                axis=0))

    def graph(self):
        self.ui.BscanWidget.setImage(
            20 *
            np.log10(
                np.rot90(self.shared_vars.b_scan) +
                float(
                    self.ui.log10_coef.text())))
        self.shared_vars.aspect_ratio = float(self.ui.aspect_ratio.text())
        self.ui.BscanWidget.view.setAspectLocked(
            ratio=self.shared_vars.aspect_ratio)
        self.ui.logbrowser.append('Data visualized successfully')

    def set_acq_parameters(self):
        self.shared_vars.param1 = self.ui.param1.text()

    def set_init_parameters(self):
        # READ OUT GUI PARAMS TO SET THEM
        # Part of buff <self.shared_vars.samples_num>
        self.shared_vars.sample_min = int(self.ui.sampling_start_ui.text())
        self.shared_vars.sample_max = int(self.ui.sampling_stop_ui.text())
        self.shared_vars.sig_delay = str(self.ui.trig_delay.text())

    def set_parameters_to_save(self):
        # READ OUT GUI PARAMS TO SET THEM
        # Part of buff <self.shared_vars.samples_num>
        self.shared_vars.idle_time = float(self.ui.a_idle_time.text())
        self.shared_vars.wave_left = float(self.ui.wave_left_ui.text())
        self.shared_vars.wave_right = float(self.ui.wave_right_ui.text())
        self.shared_vars.sample_min = int(self.ui.sampling_start_ui.text())
        self.shared_vars.sample_max = int(self.ui.sampling_stop_ui.text())
        self.shared_vars.samples_num = self.shared_vars.sample_max - \
            self.shared_vars.sample_min
        self.shared_vars.sig_delay = str(self.ui.trig_delay.text())
        self.shared_vars.avg_num = int(self.ui.avg_num_ui.text())
        self.shared_vars.ref_avg_num = int(self.ui.ref_avg_num_ui.text())
        self.shared_vars.x_step = float(self.ui.x_step_ui.text())
        self.shared_vars.xstart_coordinate = float(
            self.ui.x_start_pos_ui.text())
        self.shared_vars.xstop_coordinate = float(self.ui.x_stop_pos_ui.text())
        self.shared_vars.ystep = float(self.ui.y_step.text())
        self.shared_vars.ystart_coordinate = float(
            self.ui.ui_y_start_pos.text())
        self.shared_vars.ystop_coordinate = float(self.ui.ui_y_stop_pos.text())
        self.shared_vars.gaussian_sigma = float(self.ui.gaussian_std_ui.text())
        self.shared_vars.gaussian_pos = float(self.ui.gaussian_pos_ui.text())
        self.shared_vars.param1 = self.ui.param1.text()
        self.shared_vars.filename = self.ui.filenameline.text()
        self.shared_vars.log_coeff = float(self.ui.log10_coef.text())
        self.shared_vars.aspect_ratio = float(self.ui.aspect_ratio.text())

    def reset_parameters(self):
        # READ OUT GUI PARAMS TO SET THEM
        # Part of buff <self.shared_vars.samples_num>
        self.shared_vars.sample_min = int(self.ui.sampling_start_ui.text())
        self.shared_vars.sample_max = int(self.ui.sampling_stop_ui.text())
        self.shared_vars.samples_num = self.shared_vars.sample_max - \
            self.shared_vars.sample_min
        print(self.shared_vars.samples_num)
        self.shared_vars.scan_range = np.flip(
            np.arange(
                self.shared_vars.xstop_coordinate,
                self.shared_vars.xstart_coordinate +
                self.shared_vars.x_step,
                self.shared_vars.x_step),
            0)
        self.shared_vars.refer_arr = np.zeros(
            [self.shared_vars.ref_avg_num, self.shared_vars.samples_num])
        # spectarr = (c_float*510)()
        self.shared_vars.data = np.zeros(
            [self.shared_vars.samples_num, self.shared_vars.avg_num])
        self.shared_vars.interm_output = np.zeros(
            [self.shared_vars.samples_num, len(self.shared_vars.scan_range)])
        self.shared_vars.output_fft = np.zeros(
            [self.shared_vars.samples_num, len(self.shared_vars.scan_range)])
        self.shared_vars.gaussian_window = np.exp(-1 / 2 * ((np.linspace(-(self.shared_vars.samples_num - 1) / 2,
                                                                         (self.shared_vars.samples_num - 1) / 2,
                                                                         self.shared_vars.samples_num) - self.shared_vars.gaussian_pos) / (4 * self.shared_vars.gaussian_sigma))**2)
        self.ui.gaussian.setData(
            decimate(
                np.interp(
                    self.shared_vars.gaussian_window,
                    (self.shared_vars.gaussian_window.min(),
                     self.shared_vars.gaussian_window.max()),
                    (0,
                     1)),
                self.shared_vars.decimation_factor,
                axis=0))
        self.shared_vars.sig_delay = str(self.ui.trig_delay.text())

    def get_startpos(self):
        self.shared_vars.ystart_coordinate = float(
            self.ui.ui_y_start_pos.text())
        self.shared_vars.xstart_coordinate = float(
            self.ui.x_start_pos_ui.text())

    def set_octparameters(self):
        self.shared_vars.sample_min = int(self.ui.sampling_start_ui.text())
        self.shared_vars.sample_max = int(self.ui.sampling_stop_ui.text())
        self.shared_vars.samples_num = self.shared_vars.sample_max - \
            self.shared_vars.sample_min
        if self.ui.AveragingCheckBox.isChecked():
            print('Averaging mode')
            # Number of averaged pixels
            self.shared_vars.avg_num = int(self.ui.avg_num_ui.text())
        else:
            print('No averaging')
            self.shared_vars.avg_num = 1  # Number of averaged pixels

        self.shared_vars.ref_avg_num = int(self.ui.ref_avg_num_ui.text())
        print(self.shared_vars.ref_avg_num)
        self.shared_vars.x_step = float(self.ui.x_step_ui.text())
        self.shared_vars.xstart_coordinate = float(
            self.ui.x_start_pos_ui.text())
        self.shared_vars.xstop_coordinate = float(self.ui.x_stop_pos_ui.text())

        self.shared_vars.ystep = float(self.ui.y_step.text())
        self.shared_vars.ystart_coordinate = float(
            self.ui.ui_y_start_pos.text())
        self.shared_vars.ystop_coordinate = float(self.ui.ui_y_stop_pos.text())

        self.shared_vars.idle_time = float(self.ui.a_idle_time.text())

        self.shared_vars.data = np.zeros(
            [self.shared_vars.samples_num, self.shared_vars.avg_num])
        self.shared_vars.refer_arr = np.zeros(
            [self.shared_vars.ref_avg_num, self.shared_vars.samples_num])
        self.shared_vars.scan_range = np.flip(
            np.arange(
                self.shared_vars.xstop_coordinate,
                self.shared_vars.xstart_coordinate +
                self.shared_vars.x_step,
                self.shared_vars.x_step),
            0)

        self.shared_vars.interm_output = np.zeros(
            [self.shared_vars.samples_num, len(self.shared_vars.scan_range)])
        self.shared_vars.output_fft = np.zeros(
            [self.shared_vars.samples_num, len(self.shared_vars.scan_range)])

    def set_postprocessparameters(self):
        self.shared_vars.sample_min = int(self.ui.sampling_start_ui.text())
        self.shared_vars.sample_max = int(self.ui.sampling_stop_ui.text())
        self.shared_vars.samples_num = self.shared_vars.sample_max - \
            self.shared_vars.sample_min

        self.shared_vars.wave_left = float(self.ui.wave_left_ui.text())
        self.shared_vars.wave_right = float(self.ui.wave_right_ui.text())
        self.shared_vars.gaussian_sigma = float(self.ui.gaussian_std_ui.text())
        self.shared_vars.gaussian_pos = float(self.ui.gaussian_pos_ui.text())
        self.ui.logbrowser.append(
            '\nBandwidth SET, LOW Wavelength: ' + str(self.shared_vars.wave_left))
        self.ui.logbrowser.append(
            'Bandwidth SET, HIGH Wavelength: ' +
            str(self.shared_vars.wave_right))
        self.ui.logbrowser.append(
            'Gaussian window width (STD): ' +
            str(self.shared_vars.gaussian_sigma))
        self.ui.logbrowser.append(
            'Gaussian window position: ' + str(self.shared_vars.gaussian_pos) + '\n')

        self.shared_vars.gaussian_window = np.exp(-1 / 2 * ((np.linspace(-(self.shared_vars.samples_num - 1) / 2,
                                                                         (self.shared_vars.samples_num - 1) / 2,
                                                                         self.shared_vars.samples_num) - self.shared_vars.gaussian_pos) / (4 * self.shared_vars.gaussian_sigma))**2)
        self.ui.gaussian.setData(
            decimate(
                np.interp(
                    self.shared_vars.gaussian_window,
                    (self.shared_vars.gaussian_window.min(),
                     self.shared_vars.gaussian_window.max()),
                    (0,
                     1)),
                self.shared_vars.decimation_factor,
                axis=0))

    def preset2_mode(self):
        self.shared_vars.wave_left = 1850
        self.shared_vars.wave_right = 2150
        self.shared_vars.gaussian_sigma = 200
        self.shared_vars.gaussian_pos = 0
        self.ui.wave_right_ui.setText(str(self.shared_vars.wave_right))
        self.ui.wave_left_ui.setText(str(self.shared_vars.wave_left))
        self.ui.gaussian_std_ui.setText(str(self.shared_vars.gaussian_sigma))
        self.ui.aspect_ratio.setText('1')
        self.shared_vars.gaussian_window = np.exp(-1 / 2 * ((np.linspace(-(self.shared_vars.samples_num - 1) / 2,
                                                                         (self.shared_vars.samples_num - 1) / 2,
                                                                         self.shared_vars.samples_num) - self.shared_vars.gaussian_pos) / (4 * self.shared_vars.gaussian_sigma))**2)
        self.ui.gaussian.setData(
            decimate(
                np.interp(
                    self.shared_vars.gaussian_window,
                    (self.shared_vars.gaussian_window.min(),
                     self.shared_vars.gaussian_window.max()),
                    (0,
                     1)),
                self.shared_vars.decimation_factor,
                axis=0))

    def preset1_mode(self):
        self.shared_vars.wave_left = 3720
        self.shared_vars.wave_right = 4200
        self.shared_vars.gaussian_sigma = 1000
        self.shared_vars.gaussian_pos = 0
        self.ui.wave_right_ui.setText(str(self.shared_vars.wave_right))
        self.ui.wave_left_ui.setText(str(self.shared_vars.wave_left))
        self.ui.gaussian_std_ui.setText(str(self.shared_vars.gaussian_sigma))
        self.ui.gaussian_pos_ui.setText(str(self.shared_vars.gaussian_pos))
        self.ui.aspect_ratio.setText('0.5')
        self.shared_vars.gaussian_window = np.exp(-1 / 2 * ((np.linspace(-(self.shared_vars.samples_num - 1) / 2,
                                                                         (self.shared_vars.samples_num - 1) / 2,
                                                                         self.shared_vars.samples_num) - self.shared_vars.gaussian_pos) / (4 * self.shared_vars.gaussian_sigma))**2)
        self.ui.gaussian.setData(
            decimate(
                np.interp(
                    self.shared_vars.gaussian_window,
                    (self.shared_vars.gaussian_window.min(),
                     self.shared_vars.gaussian_window.max()),
                    (0,
                     1)),
                self.shared_vars.decimation_factor,
                axis=0))

    def stop_spectrometer(self):
        print('Stopped')
        self.shared_vars.flag = 1

    def resarray(self):
        self.ui.logbrowser.append('Parameters (re)set, (re)start')
        self.shared_vars.flag = 0
        self.ui.logbrowser.append(str(self.shared_vars.param1))

    def status_ui_measurements_started(self):
        self.ui.InitButton.setEnabled(False)
        self.ui.SetOCTParamsButton.setEnabled(False)
        self.ui.ApplyProcButton.setEnabled(False)

    def status_ui_measurements_done(self):
        self.ui.InitButton.setEnabled(True)
        self.ui.SetOCTParamsButton.setEnabled(True)
        self.ui.ApplyProcButton.setEnabled(True)

    def wait_for_threads(self):
        self.buffer_thread.wait()
        self.save_thread.wait()
        self.bscan_measurement_thread.wait()
        self.cscan_measurement_thread.wait()
        self.save_params_thread.wait()
        self.referencing_thread.wait()
        self.sys_init_thread.wait()
        self.ystage_init_thread.wait()
        self.post_process_thread.wait()
        self.y_stage_up.wait()
        self.y_stage_down.wait()
        self.y_axis_move_to.wait()
        self.x_axis_move_to.wait()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Exit', 'Do you want to exit?')
        if reply == QMessageBox.Yes:
            event.accept()
            self.shared_vars.flag = 1
            self.shared_vars.inloop_flag = 0
            self.shared_vars.measurement_flag = 0
            self.wait_for_threads()
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
        for i in range(0, len(self.shared_vars.refer_arr)):
            time.sleep(self.shared_vars.idle_time)
            if self.shared_vars.measurement_flag == 0:
                self.shared_vars.measurement_flag = 1
                break
            self.shared_vars.refer_arr[i, :] = self.shared_vars.buffer_signal

            self.refprogress = (i + 1) / len(self.shared_vars.refer_arr) * 100
            self.refprog.emit(self.refprogress)

        self.shared_vars.reference_spectrum = np.mean(
            self.shared_vars.refer_arr[:i, :], 0)
        self.refdone.emit(self.refprogress)


class YMoveUpByThread(QtCore.QThread):
    status = QtCore.Signal(object)

    def __init__(self, shared_vars):
        super().__init__()
        self.shared_vars = shared_vars

    def run(self):
        print('Moved up by 0.5 mm')
        self.msg = 'Moved up by 0.5 mm'
        self.status.emit(self.msg)


class YMoveDownByThread(QtCore.QThread):
    status = QtCore.Signal(object)

    def __init__(self, shared_vars):
        super().__init__()
        self.shared_vars = shared_vars

    def run(self):
        print('Moved down by 0.5 mm')
        self.msg = 'Moved down by 0.5 mm'
        self.status.emit(self.msg)


class YPositionToThread(QtCore.QThread):
    status = QtCore.Signal(object)

    def __init__(self, shared_vars):
        super().__init__()
        self.shared_vars = shared_vars

    def run(self):
        self.msg = 'Moved to start Y position'
        self.status.emit(self.msg)


class XPositionToThread(QtCore.QThread):
    status = QtCore.Signal(object)

    def __init__(self, shared_vars):
        super().__init__()
        self.shared_vars = shared_vars

    def run(self):
        self.msg = 'Moved to start X position: ' + \
            str(self.shared_vars.xstart_coordinate)
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
        self.shared_vars.raw_data = None
        if len(self.shared_vars.data) == len(
                self.shared_vars.reference_spectrum):
            self.y_scan_range = np.flip(
                np.arange(
                    self.shared_vars.ystop_coordinate,
                    self.shared_vars.ystart_coordinate +
                    self.shared_vars.ystep,
                    self.shared_vars.ystep),
                0)

            self.ascan_avg_arr = np.zeros([self.shared_vars.samples_num,
                                          self.shared_vars.avg_num,
                                          len(self.shared_vars.scan_range)])

            self.volume_scan = np.zeros(
                [len(self.y_scan_range), self.shared_vars.z_sample_num, len(self.shared_vars.scan_range)])

            totalmeasurements = len(self.y_scan_range) * \
                len(self.shared_vars.scan_range)

            # START MEASUREMENT
            start_time = time.time()
            len_counter = 1
            z_counter = 1

            with OCTLib(self.shared_vars.reference_spectrum, self.shared_vars.wave_left, self.shared_vars.wave_right, self.shared_vars.cal_vector, self.shared_vars.boundaries, self.shared_vars.samples_num, gauss_win_in=self.shared_vars.gaussian_window) as oct_process:
                for self.y_pos in range(0, len(self.y_scan_range)):
                    # Scanning along Y (if super ystage is defined)
                    # global ystage
                    # ystage.moveto(self.y_scan_range[self.y_pos])
                    print(self.y_scan_range[self.y_pos])
                    print(self.y_pos)

                    # motor.move_to(self.y_scan_range[self.y_pos], True)

                    if self.shared_vars.measurement_flag == 0:
                        self.shared_vars.measurement_flag = 1
                        break

                    for itn in range(0, len(self.shared_vars.scan_range)):
                        # Scanning along X (if super xstage is defined)
                        # global xstage
                        # xstage.moveto(self.shared_vars.scan_range[itn])

                        # print(
                        #     'Position:',
                        #     round(
                        #         self.shared_vars.scan_range[itn],
                        #         3),
                        #     'mm')
                        if self.shared_vars.measurement_flag == 0:
                            break

                        for i in range(0, self.shared_vars.avg_num):
                            # print(
                            #     'Y-STEPNUM: ',
                            #     self.y_pos,
                            #     ' Position:',
                            #     round(
                            #         self.shared_vars.scan_range[itn],
                            #         3),
                            #     'mm ',
                            #     "Spectrum number: ",
                            #     i)
                            self.shared_vars.data[:,
                                                  i] = self.shared_vars.buffer_signal
                            # FOR FUTHER FFT AVERAGING
                            self.ascan_avg_arr[:, i,
                                               itn] = self.shared_vars.buffer_signal
                            time.sleep(self.shared_vars.idle_time)
                            if self.shared_vars.flag != 0:
                                break
                        self.shared_vars.interm_output[:, itn] = np.mean(
                            self.shared_vars.data, 1)
                        average_f_space = np.rot90(self.shared_vars.data, 1)
                        self.shared_vars.output_fft[:, itn] = np.mean(
                            oct_process.scan_process(oct_process.remap_to_k(average_f_space)), 0)

                        len_counter = len_counter + 1

                        self.progress = 100 * \
                            (len_counter + z_counter) / totalmeasurements
                        self.measprog.emit(self.progress)
                        if self.shared_vars.flag != 0:
                            break
                    self.to_ppost = np.rot90(self.shared_vars.interm_output, 1)
                    if self.shared_vars.flag != 0:
                        break

                    # PROCESS
                    self.shared_vars.b_scan = oct_process.scan_process(
                        oct_process.remap_to_k(self.to_ppost))
                    self.scanf = np.rot90(self.shared_vars.b_scan)

                    self.volume_scan[self.y_pos, :, :] = self.scanf[int(self.shared_vars.samples_num / 2):int(
                        self.shared_vars.samples_num / 2) + self.shared_vars.z_sample_num, :]
                    self.shared_vars.b_scan = np.flip(np.moveaxis(
                        np.flip(self.volume_scan[:self.y_pos + 1, :, :], 0), -1, 0), 1)
                    z_counter = z_counter + 1
                    if np.shape(self.shared_vars.b_scan)[1] > 0:
                        self.mdat.emit(self.progress)
                        print(np.shape(self.shared_vars.b_scan))

            self.shared_vars.scans = self.volume_scan
            # motor.move_to(self.y_scan_range[0])

            self.shared_vars.b_scan = np.moveaxis(
                np.flip(self.volume_scan, 0), -1, 0)
            print('3D measurement completed')
            self.ms_msg = 'Volumetric scan is DONE in ' + \
                "--- %s seconds ---" % (time.time() - start_time)
            self.meas_status.emit(self.ms_msg)
            self.progress = 100
            self.measprog.emit(self.progress)
        else:
            self.ms_msg = 'ERROR - Referencing is needed'
            self.meas_status.emit(self.ms_msg)


class BScanMeasureThread(QtCore.QThread):
    measprog = QtCore.Signal(object)
    mdat = QtCore.Signal(object)
    meas_status = QtCore.Signal(object)

    def __init__(self, shared_vars):
        super().__init__()
        self.shared_vars = shared_vars

    def run(self):
        while True:
            if self.shared_vars.flag != 0:
                break
            # err = 0
            start_time = time.time()
            if len(self.shared_vars.data) == len(
                    self.shared_vars.reference_spectrum):
                self.ms_msg = 'Measurements started...\n' + 'b_scan length: ' + \
                    str(self.shared_vars.xstart_coordinate - self.shared_vars.xstop_coordinate) + 'mm\n' + 'Averaging: ' + str(self.shared_vars.avg_num)
                self.meas_status.emit(self.ms_msg)

                with OCTLib(self.shared_vars.reference_spectrum, self.shared_vars.wave_left, self.shared_vars.wave_right, self.shared_vars.cal_vector, self.shared_vars.boundaries, self.shared_vars.samples_num, gauss_win_in=self.shared_vars.gaussian_window) as oct_process:
                    for itn in range(0, len(self.shared_vars.scan_range)):
                        # Scanning along X (if super xstage is defined)
                        # global xstage
                        # xstage.moveto(self.shared_vars.scan_range[itn])

                        # logging.info(
                        #     'Position: %s mm; Errors: %s; Av.self.shared_vars.avg_num: %s; Gaussian window: %s; WinWidth: %s',
                        #     round(
                        #         self.shared_vars.scan_range[itn],
                        #         2),
                        #     err,
                        #     self.shared_vars.avg_num,
                        #     self.shared_vars.gaussian_sigma,
                        #     self.shared_vars.gaussian_pos)
                        self.progress = 100 * (itn + 1) / \
                            len(self.shared_vars.scan_range)
                        self.measprog.emit(self.progress)

                        if self.shared_vars.measurement_flag == 0:
                            self.shared_vars.measurement_flag = 1
                            break
                        for i in range(
                                0, self.shared_vars.avg_num):  # Averaging
                            if self.shared_vars.flag != 0:
                                break
                            if self.shared_vars.inloop_flag == 0:
                                self.shared_vars.inloop_flag = 1
                                break
                            time.sleep(self.shared_vars.idle_time)

                            self.shared_vars.data[:,
                                                  i] = self.shared_vars.buffer_signal
                        self.shared_vars.interm_output[:, itn] = np.mean(
                            self.shared_vars.data, 1)

                        self.average_f_space = np.rot90(
                            self.shared_vars.data, 1)
                        self.shared_vars.output_fft[:, itn] = np.mean(
                            oct_process.scan_process(oct_process.remap_to_k(self.average_f_space)), 0)
                        if self.shared_vars.flag != 0:
                            break
                    self.interm_output = np.rot90(
                        self.shared_vars.interm_output, 1)
                    self.shared_vars.raw_data = np.copy(self.interm_output)

                    # PROCESS
                    self.shared_vars.b_scan = oct_process.scan_process(
                        oct_process.remap_to_k(self.interm_output))
                self.scanf = np.rot90(self.shared_vars.b_scan, 3)

                # AVERAGE WITH MEAN FOURIER SPACE
                self.avg_of_spaces = np.mean([self.scanf[int(self.shared_vars.samples_num /
                                                             2):int(self.shared_vars.samples_num /
                                                                    2 +
                                                                    self.shared_vars.z_sample_num), :], self.shared_vars.output_fft[int(self.shared_vars.samples_num /
                                                                                                                                        2 +
                                                                                                                                        0):int(self.shared_vars.samples_num /
                                                                                                                                               2 +
                                                                                                                                               self.shared_vars.z_sample_num +
                                                                                                                                               0), :]], 0)
                self.shared_vars.scans = np.array([self.avg_of_spaces, self.scanf[int(self.shared_vars.samples_num /
                                                                                      2):int(self.shared_vars.samples_num /
                                                                                             2 +
                                                                                             self.shared_vars.z_sample_num), :], self.shared_vars.output_fft[int(self.shared_vars.samples_num /
                                                                                                                                                                 2 +
                                                                                                                                                                 0):int(self.shared_vars.samples_num /
                                                                                                                                                                        2 +
                                                                                                                                                                        self.shared_vars.z_sample_num +
                                                                                                                                                                        0), :]])

                # alternative: b_scan = np.moveaxis(np.flip(self.shared_vars.scans, 0), -1, 0)
                self.shared_vars.b_scan = self.shared_vars.scans.transpose(
                    2, 0, 1)
                print("--- %s seconds ---" % (time.time() - start_time))
                self.ms_msg = 'DONE in ' + \
                    "--- %s seconds ---" % (time.time() - start_time)
                self.meas_status.emit(self.ms_msg)
                self.mdat.emit(self.progress)
            else:
                self.ms_msg = 'ERROR - Referencing is needed'
                self.meas_status.emit(self.ms_msg)
                break
            if not self.shared_vars.run_continuous:
                break


class PostProcessingThread(QtCore.QThread):
    request_parameters = QtCore.Signal(object)

    def __init__(self, shared_vars):
        super().__init__()
        self.shared_vars = shared_vars

    def run(self):
        self.request_parameters.emit(self)
        print(self.shared_vars.wave_left)
        print(self.shared_vars.wave_right)
        print(self.shared_vars.gaussian_sigma)
        print(self.shared_vars.gaussian_pos)
        # PROCESS
        if self.shared_vars.raw_data is not None:
            self.local_topost = np.copy(self.shared_vars.raw_data)
            with OCTLib(self.shared_vars.reference_spectrum, self.shared_vars.wave_left, self.shared_vars.wave_right, self.shared_vars.cal_vector, self.shared_vars.boundaries, self.shared_vars.samples_num, gauss_win_in=self.shared_vars.gaussian_window) as oct_process:
                self.local_scan = oct_process.scan_process(
                    oct_process.remap_to_k(self.local_topost))
            self.local_scanf = np.rot90(self.local_scan)
            # AVERAGE WITH MEAN FOURIER SPACE
            self.local_purescn = self.local_scanf[int(self.shared_vars.samples_num / 2):int(
                self.shared_vars.samples_num / 2 + self.shared_vars.z_sample_num), :]
            self.shared_vars.b_scan = self.local_purescn
            del self.local_topost
        else:
            print('No rawdata stored in memory')


class YstageInitThread(QtCore.QThread):
    initdone = QtCore.Signal(object)
    init_status = QtCore.Signal(object)

    def __init__(self, shared_vars):
        super().__init__()
        self.shared_vars = shared_vars

    def run(self):
        try:
            print('Y stage initialization')
            # Initialize your YStage here

            # Example of how Y stage cam be loaded and initialized (artificial superstage)
            # try:
            #     global ystage
            #     xstage = superstage.init(serial)
            #     self.init_msg = '\nY stage is initialized\n'
            #     self.init_status.emit(self.init_msg)
            # except BaseException:
            #     self.init_msg = '\nY stage not found\n'
            #     self.init_status.emit(self.init_msg)
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

    def __init__(self, shared_vars, buffer_thread):
        super().__init__()
        self.shared_vars = shared_vars
        self.buffer_thread = buffer_thread

    def run(self):
        # Example of how X stage cam be loaded and initialized (artificial superstage)
        # try:
        #     global xstage
        #     xstage = superstage.init(serial)
        #     self.init_msg = '\nX stage is initialized\n'
        #     self.init_status.emit(self.init_msg)
        # except BaseException:
        #     self.init_msg = '\nX stage not found\n'
        #     self.init_status.emit(self.init_msg)

        # INIT OF CAMERA
        # #DAQ CONFIGURATION
        try:
            self.buffer_thread.cam_init()  # Here the source is initialized(exeplified for camera that is defined in the bufffer thread)
            self.init_msg = '\nCamera is successfully initialized\nReady to measure...\n'
            self.init_status.emit(self.init_msg)
        except BaseException:
            self.init_msg = '\nCamera not found\n'
            self.init_status.emit(self.init_msg)
        if self.shared_vars.cal_vector is not None and self.shared_vars.boundaries is not None:
            self.init_msg = 'Calibration vector loaded'
            self.init_status.emit(self.init_msg)
        else:
            self.init_msg = 'Calibration vector not found'
            self.init_status.emit(self.init_msg)

        # Example of initializing something
        self.init_msg = 'Shutter system is initialized'
        self.init_status.emit(self.init_msg)

        print('\nMoving to start position...')
        print('\nReady to measure...')
        self.init_msg = '\nHardware is successfully initialized\nReady to measure...\n'
        self.init_status.emit(self.init_msg)
        self.initdone.emit(self)


class SaveDataThread(QtCore.QThread):
    status = QtCore.Signal(object)

    def __init__(self, shared_vars):
        super().__init__()
        self.shared_vars = shared_vars

    def run(self):
        if self.shared_vars.scans is not None and np.mean(
                self.shared_vars.scans) != 0:
            try:
                np.save(
                    self.shared_vars.directory +
                    '/' +
                    self.shared_vars.filename +
                    datetime.now().strftime('%Y-%m-%d_%H-%M_%S') +
                    '.npy',
                    self.shared_vars.scans)
                print(
                    'Saved as ' +
                    self.shared_vars.directory +
                    '/' +
                    self.shared_vars.filename +
                    datetime.now().strftime('%Y-%m-%d_%H-%M_%S') +
                    '.npy')
                self.msg = 'Saved in ' + self.shared_vars.directory
                self.status.emit(self.msg)
                if np.shape(self.shared_vars.scans)[0] > 3:
                    self.scans_to_save = 20 * \
                        np.log10(np.copy(self.shared_vars.scans) + self.shared_vars.log_coeff)
                    self.scans_to_save = self.scans_to_save - \
                        np.min(self.scans_to_save)
                    self.scans_to_save = self.scans_to_save / \
                        np.max(self.scans_to_save) * 65536
                    self.scans_to_save = self.scans_to_save[:, :, :]
                    self.scans_to_save = self.scans_to_save.astype(np.uint16)
                    try:
                        tif.imwrite(
                            self.shared_vars.directory +
                            '/' +
                            self.shared_vars.filename +
                            datetime.now().strftime('%Y-%m-%d_%H-%M_%S') +
                            '.tif',
                            self.scans_to_save,
                            photometric='minisblack')
                        self.msg = 'Tif volume saved in ' + self.shared_vars.directory
                        self.status.emit(self.msg)
                    except BaseException:
                        self.msg = 'Tif volume saved in ' + './data_output/'
                        self.status.emit(self.msg)
                        tif.imwrite(
                            './data_output/' +
                            self.shared_vars.filename +
                            datetime.now().strftime('%Y-%m-%d_%H-%M_%S') +
                            '.tif',
                            self.scans_to_save,
                            photometric='minisblack')
            except BaseException:
                np.save(
                    './data_output/' +
                    self.shared_vars.filename +
                    datetime.now().strftime('%Y-%m-%d_%H-%M_%S') +
                    '.npy',
                    self.shared_vars.scans)
                self.msg = 'Saved in ' + './data_output/'
                self.status.emit(self.msg)
                if np.shape(self.shared_vars.scans)[0] > 3:
                    self.scans_to_save = 20 * \
                        np.log10(np.copy(self.shared_vars.scans) + self.shared_vars.log_coeff)
                    self.scans_to_save = self.scans_to_save - \
                        np.min(self.scans_to_save)
                    self.scans_to_save = self.scans_to_save / \
                        np.max(self.scans_to_save) * 65536
                    self.scans_to_save = self.scans_to_save[:, :, :]
                    self.scans_to_save = self.scans_to_save.astype(np.uint16)
                    self.msg = 'Tif volume saved in ' + './data_output/'
                    self.status.emit(self.msg)
                    tif.imwrite(
                        './data_output/' +
                        self.shared_vars.filename +
                        datetime.now().strftime('%Y-%m-%d_%H-%M_%S') +
                        '.tif',
                        self.scans_to_save,
                        photometric='minisblack')
        else:
            print('Empthy data')
            self.msg = 'Empthy data, cannot save'
            self.status.emit(self.msg)


class SaveParamsThread(QtCore.QThread):
    status = QtCore.Signal(object)

    def __init__(self, shared_vars):
        super().__init__()
        self.shared_vars = shared_vars

    def run(self):
        np.save('./settings/ref.npy', self.shared_vars.reference_spectrum)
        self.shared_vars.save_parameters()


if __name__ == "__main__":
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_FONT_DPI"] = "96"
    app = QtCore.QCoreApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
        app.setWindowIcon(QtGui.QIcon("icon.ico"))
    qtmodern.styles.dark(app)
    mwins = win()
    mwins = qtmodern.windows.ModernWindow(mwins)
    qr = mwins.frameGeometry()
    cp = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
    qr.moveCenter(cp)
    mwins.move(qr.topLeft())
    mwins.show()
    sys.exit(app.exec())
