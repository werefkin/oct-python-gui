import numpy as np


class SharedVariables:
    def __init__(self):
        self.flag = 0
        self.buffer_signal = np.ones(16384)
        self.sample_min = 0
        self.sample_max = 16384
