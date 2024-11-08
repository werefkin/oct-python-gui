import numpy as np
from scipy.interpolate import interp1d


class OCTLib:
    def __init__(self, ref_spectrum, wave_min, wave_max, cal_vector=None, boundaries=None, sa_num=16384, gauss_win_in=None, c2=0, c3=0, kind1='cubic'):
        self.ref_spectrum = ref_spectrum
        self.wave_min = wave_min
        self.wave_max = wave_max
        self.cal_vector = cal_vector
        self.boundaries = boundaries
        self.sa_num = sa_num
        self.kind1 = kind1
        self.gauss_win = gauss_win_in
        self.spectral_interferograms = None
        self.c2 = float(c2)
        self.c3 = float(c3)

    def dispersion_compensation(self, spectral_data, k, phase_comp_coeff):
        """
        Compensates for dispersion in the spectral interferogram.

        Parameters:
        - spectral_data: The original spectral interferogram (1D numpy array).
        - k: Wavenumber vector (1D numpy array, corresponding to the spectral_data).
        - phase_comp_coeff: Dispersion compensation coefficients (tuple: (c2, c3)).

        Returns:
        - Compensated spectral interferogram (1D numpy array).
        """

        # Phase
        ic2, ic3 = phase_comp_coeff
        phase_correction = np.exp(1j * (ic2 * k**2 + ic3 * k**3))

        # Apply the phase correction in the frequency domain
        compensated_spectral_data = spectral_data * phase_correction

        return compensated_spectral_data

    def remap_to_k(self, data):
        data = data - self.ref_spectrum
        if self.cal_vector is not None and self.boundaries is not None:
            remap_interp_func = interp1d(self.cal_vector, data[:, self.boundaries[0]:self.boundaries[-1]],
                                         axis=1, kind=self.kind1, fill_value="extrapolate")
            spectral_interferograms = remap_interp_func(np.linspace(self.boundaries[0], self.boundaries[-1], len(self.cal_vector), endpoint=True))
            NN = int((self.sa_num - len(self.cal_vector)) / 2)
            spectral_interferograms = np.pad(spectral_interferograms, ((0, 0), (NN, self.sa_num - NN - len(self.cal_vector))), 'constant')
        else:
            lambda_space_rang = np.linspace(self.wave_min, self.wave_max, self.sa_num, endpoint=True)
            k_space_rang = 1 / lambda_space_rang
            wn_corr = np.linspace(k_space_rang[0], k_space_rang[-1], self.sa_num)
            remap_interp_func = interp1d(k_space_rang, data, axis=1, kind=self.kind1, fill_value="extrapolate")
            spectral_interferograms = remap_interp_func(wn_corr)
        self.spectral_interferograms = spectral_interferograms
        return spectral_interferograms

    def scan_process(self, lin_spe_int):
        """
        lin_spe_int - spectrums in k-space
        typ - 's' - substraction of the envelope (less noise), typ='d' is division

        RETURNS OCT B-SCAN

        """
        phase_comp_coeff = [self.c2, self.c3]
        k = np.linspace(1e7 / self.wave_min, 1e7 / self.wave_max, self.sa_num)

        lin_spe_int_co = self.dispersion_compensation(lin_spe_int, k, phase_comp_coeff)

        # compute the FFT of the windowed signal
        scan = np.abs(np.fft.fftshift(np.fft.fft(lin_spe_int_co * self.gauss_win, axis=1), axes=1))
        # Save data in to array
        return scan

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass
