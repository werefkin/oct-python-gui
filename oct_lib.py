
"""
LIBRARY FUNCTIONS:

    1. "remap_to_k" converts spectral interferograms measured in wavelengths (with subtraction of the reference)
    in wavenumbers
    performing interpolation to get equidistant sampling in k-space
    OUTPUT is spectral interferograms in wavenumbers
    in this code wavelengths assumed to be linear

    2. scanProcess performs postprocessing of the signal in following order:
    (Gaussian window --> FFT) -- Removed: Hilbert transform --> Analytic signal --> Envelope --> High Pass Filter)

    3. depthAxis calculates depth axis you have after FFT according to number of pixels and spectrum bandwidth

@author: r.zor
"""

import numpy as np
from scipy.interpolate import interp1d
# from scipy.signal import hilbert

kind1 = "quadratic"


def remap_to_k(data, ref_spectrum, wave_min, wave_max, cal_vector=None, boundaries=None, sa_num=16384):
    data = data - ref_spectrum
    if cal_vector is not None and boundaries is not None:

        # print("Calibration-vector based")
        remap_interp_func = interp1d(cal_vector,
                                     data[:,
                                          boundaries[0]:boundaries[-1]],
                                     axis=1,
                                     kind=kind1,
                                     fill_value="extrapolate")
        spectral_interferograms = remap_interp_func(np.linspace(
            boundaries[0], boundaries[-1], len(cal_vector), endpoint=True))
        NN = (sa_num - len(cal_vector)) / 2
        spectral_interferograms = np.pad(
            spectral_interferograms, ((0, 0), (int(NN), int(NN))), 'constant')
    else:
        # print("Standard processing")
        lambda_space_rang = np.linspace(wave_min, wave_max, sa_num, endpoint=True)
        k_space_rang = 1 / lambda_space_rang
        wn_corr = np.linspace(k_space_rang[0], k_space_rang[-1], sa_num)
        remap_interp_func = interp1d(
            k_space_rang,
            data,
            axis=1,
            kind=kind1,
            fill_value="extrapolate")
        spectral_interferograms = remap_interp_func(wn_corr)
    return (spectral_interferograms)


def scanProcess(lin_spe_int, gauss_win):
    """
    lin_spe_int - spectrums in k-space
    typ - 's' - substraction of the envelope (less noise), typ='d' is division

    RETURNS OCT B-SCAN

    """
    # CREATE ARRAYS FOR DATA
    scan = np.zeros([len(lin_spe_int), len(lin_spe_int[0])])

    # compute the windowed signal
    # compute the FFT of the windowed signal
    scan = np.abs(np.fft.fftshift(np.fft.fft(lin_spe_int * gauss_win, axis=1), axes=1))
    # Save data in to array
    return scan


def norma(d, norma):
    d -= np.min(d)
    if norma == 1:
        d = d / np.max(d)
    return d
