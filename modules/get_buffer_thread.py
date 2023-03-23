import numpy as np
from PySide6 import QtCore
from scipy.signal import chirp


class GetBufferThread(QtCore.QThread):

    def __init__(self, shared_vars):
        super().__init__()
        self.shared_vars = shared_vars

    def cam_init(self):
        self.device = True

    def run(self):
        self.active = True
        # f0 frequency range (tilted plate shaped)
        f_start_range1 = np.linspace(20, 2, self.shared_vars.samples_num, endpoint=True)
        f_start_range2 = np.linspace(40, 20, self.shared_vars.samples_num, endpoint=True)
        offset = 0.5   # aka plate thickness
        time = np.linspace(0, 12, self.shared_vars.samples_num)  # time
        env = np.exp(-1 / 2 * ((time - 6) / (1.5 * 1))**2)
        c_k = 10

        while self.shared_vars.flag == 0:
            for i in range(self.shared_vars.samples_num):
                self.shared_vars.buffer_signal = 2 * env + \
                    0.2 * env * \
                    (chirp(time, f0=f_start_range1[i], f1=f_start_range1[i] / c_k, t1=10, method='linear') +
                     chirp(time, f0=f_start_range2[i] + offset, f1=(f_start_range2[i] + offset) / c_k, t1=10, method='linear')) + \
                    np.random.normal(0, 0.03, self.shared_vars.samples_num)

            self.shared_vars.buffer_signal = np.random.rand(16384)[self.shared_vars.sample_min: self.shared_vars.sample_max]
