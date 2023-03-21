import numpy as np
from PySide6 import QtCore


class GetBufferThread(QtCore.QThread):

    def __init__(self, shared_vars):
        super().__init__()
        self.shared_vars = shared_vars

    def run(self):
        self.active = True
        while self.shared_vars.flag == 0:
            self.shared_vars.buffer_signal = np.random.rand(16384)[self.shared_vars.sample_min: self.shared_vars.sample_max]
