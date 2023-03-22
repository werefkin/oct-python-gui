import numpy as np
import pickle


class SharedVariables:
    def __init__(self):
        # Load variables from a file
        self.flag = 0  # global app flag to stop all the running threads if closeEvent happens
        self.measurement_flag = 1  # flag to abort measurement
        self.inloop_flag = 1  # flag to abort measurement inside a long loop
        self.idle_time = 0.05  # a-scan idle time (time deley between a-scans); as the system is async the buffer just sleeps while the measurement is done
        self.decimation_factor = 16  # to downsample Live signals (more efficient plotting)

        self.sample_min = 0  # min sample num in the signal
        self.sample_max = 16384  # max sample num in the signal
        self.samples_num = self.sample_max - self.sample_min  # number of the samples in spectra interferogram (i.e. number of pixels for camera)

        try:
            self.reference_spectrum = np.load('./settings/ref.npy')  # load a referebce spectrum
        except BaseException:
            self.reference_spectrum = np.zeros(self.sample_max)

        self.sig_delay = 0  # signal ACQ delay parameter if needed
        self.directory = ''  # directory name (defaul: data_output of the main folder)
        self.filename = 'test'  # default save filename
        self.log_coeff = 1  # coefficient for plot
        self.param1 = 0  # param1 to be used

        self.z_sample_num = 512  # Number of pixels in depth (to limit memory use for volumetruc arrays)

        self.avg_num = 3  # Number of averaged measurements
        self.wave_left = 3235.6  # min wavelength in nm
        self.wave_right = 4200.27  # max wavelength in nm

        self.b_scan = np.load('./logo/preset.npy')[:155, :]  # load a preset b-scan
        self.scans = None  # define empthy scans container

        self.buffer_signal = np.ones(self.samples_num)  # buffer signal

        self.ref_avg_num = 50  # default number of avereges to measure reference
        self.refer_arr = np.zeros([self.ref_avg_num, self.samples_num])  # defaut referencing array

        self.data = np.zeros([self.sample_min, self.sample_max])  # default data container
        self.raw_data = None  # default raw_data container

        self.xstop_coordinate = 0  # x scanning parameter
        self.xstart_coordinate = 4  # x scanning parameter
        self.x_step = 0.04  # x scanning parameter

        self.ystart_coordinate = 4  # y scanning parameter
        self.ystop_coordinate = 0  # y scanning parameter
        self.ystep = 0.04  # y scanning parameter

        self.scan_range = np.flip(
            np.arange(
                self.xstop_coordinate,
                self.xstart_coordinate +
                self.x_step,
                self.x_step),
            0)  # x scanning range grid
        self.output_fft = np.zeros([self.samples_num, len(self.scan_range)])  # intermediate array for averaging

        self.gaussian_pos = 0  # gaussian filter position (0 is mid)
        self.gaussian_sigma = 1500  # sigma, gaussian window parameter
        self.gaussian_window = np.exp(-1 / 2 * ((np.linspace(-(self.samples_num - 1) / 2,
                                                (self.samples_num - 1) / 2,
                                                self.samples_num) - self.gaussian_pos) / (4 * self.gaussian_sigma))**2)  #

        self.interm_output = np.zeros([self.samples_num, len(self.scan_range)])  # intermediate array for averaging

        # Load calibration vector
        try:
            self.cal_vector = np.load('./settings/calibration_vector.npy')
            self.boundaries = np.load('./settings/boundaries.npy')
        except BaseException:
            self.cal_vector = None
            self.boundaries = None
            pass

    def save_parameters(self):
        # Create a dictionary of the variables you want to save
        self.PARAMs = {
            'idle_time': self.idle_time,
            'decimation_factor': self.decimation_factor,
            'sample_min': self.sample_min,
            'sample_max': self.sample_max,
            'sig_delay': self.sig_delay,
            'directory': self.directory,
            'filename': self.filename,
            'log_coeff': self.log_coeff,
            'param1': self.param1,
            'z_sample_num': self.z_sample_num,
            'avg_num': self.avg_num,
            'wave_left': self.wave_left,
            'wave_right': self.wave_right,
            'ref_avg_num': self.ref_avg_num,
            'xstop_coordinate': self.xstop_coordinate,
            'xstart_coordinate': self.xstart_coordinate,
            'x_step': self.x_step,
            'ystart_coordinate': self.ystart_coordinate,
            'ystop_coordinate': self.ystop_coordinate,
            'ystep': self.ystep,
            'gaussian_pos': self.gaussian_pos,
            'gaussian_sigma': self.gaussian_sigma}
        with open('./settings/config.cfg', 'wb') as f:
            pickle.dump(self.PARAMs, f)

    def load_parameters(self):
        try:
            with open('./settings/config.cfg', 'rb') as f:
                self.PARAMs = pickle.load(f)
                self.idle_time = self.PARAMs['idle_time']
                # self.decimation_factor = self.PARAMs['decimation_factor']
                self.decimation_factor = 16
                self.sample_min = self.PARAMs['sample_min']
                self.sample_max = self.PARAMs['sample_max']
                self.sig_delay = self.PARAMs['sig_delay']
                self.directory = self.PARAMs['directory']
                self.filename = self.PARAMs['filename']
                self.log_coeff = self.PARAMs['log_coeff']
                self.param1 = self.PARAMs['param1']
                self.z_sample_num = self.PARAMs['z_sample_num']
                self.avg_num = self.PARAMs['avg_num']
                self.wave_left = self.PARAMs['wave_left']
                self.wave_right = self.PARAMs['wave_right']
                self.ref_avg_num = self.PARAMs['ref_avg_num']
                self.xstop_coordinate = self.PARAMs['xstop_coordinate']
                self.xstart_coordinate = self.PARAMs['xstart_coordinate']
                self.x_step = self.PARAMs['x_step']
                self.ystart_coordinate = self.PARAMs['ystart_coordinate']
                self.ystop_coordinate = self.PARAMs['ystop_coordinate']
                self.ystep = self.PARAMs['ystep']
                self.gaussian_pos = self.PARAMs['gaussian_pos']
                self.gaussian_std_ui = self.PARAMs['gaussian_sigma']
        except FileNotFoundError:
            print("Config file not found. Using default parameters.")
