import numpy as np


class SharedVariables:
    def __init__(self):
        self.flag = 0  # global app flag to stop all the running threads if closeEvent happens
        self.measurement_flag = 1  # flag to abort measurement
        self.inloop_flag = 1  # flag to abort measurement inside a long loop
        self.idle_time = 0.05  # a-scan idle time (time deley between a-scans); as the system is async the buffer just sleeps while the measurement is done
        self.decimation_factor = 20  # to downsample Live signals (more efficient plotting)

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
        self.raw_data = np.zeros([self.sample_min, self.sample_max])  # default raw_data container

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
