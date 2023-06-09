# -*- coding: utf-8 -*-
"""
Created on Tue May  3 11:21:59 2022

@author: r.zor
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.signal import find_peaks
from scipy.ndimage import gaussian_filter1d
import numpy.polynomial.polynomial as poly

kind1 = "quadratic"

# Params
PV = True  # peak and valleys?
PF = True  # fit poly
height_si = 0.22  # height for single sided
height_pv = 0.002  # height for double sided (PV mode)
gauske = 20  # gaussian kernel size
pedist = 10  # distance between
# Load data
try:
    spectrum = np.load('spectrum.npy')
    interference = np.load('fringes.npy')
except BaseException:
    spectrum = np.load('./generate_calibration_vector/spectrum.npy')
    interference = np.load('./generate_calibration_vector/fringes.npy')


N = len(spectrum)  # Length

# Pure fringes
fri = interference - spectrum

# Detect peaks and make linear space (one should adjust filter and peak
# detection parameters)
# filter noise in fringe detection
signal_nonlin_wl = gaussian_filter1d(fri, gauske)


if PV:

    # Peaks and valleys detection

    grad_signal = np.gradient(signal_nonlin_wl)  # remove baseline

    peaks_p, _ = find_peaks(grad_signal, height=height_pv, distance=pedist)
    peaks_n, _ = find_peaks(-grad_signal, height=height_pv, distance=pedist)

    if peaks_p[0] > peaks_n[0]:
        x = peaks_n
        y = peaks_p
    if peaks_p[0] < peaks_n[0]:
        x = peaks_p
        y = peaks_n
    len_x = len(x)
    len_y = len(y)

    i = 0
    j = 0
    out = np.zeros(len(peaks_n) + len(peaks_p))

    # Fill the output array by alternating between x and y values
    for k in range(len(peaks_n) + len(peaks_p)):
        if k % 2 == 0:
            if i < len_x:
                out[k] = x[i]
                i += 1
            else:
                out[k] = y[j]
                j += 1
        else:
            if j < len_y:
                out[k] = y[j]
                j += 1
            else:
                out[k] = x[i]
                i += 1

    plt.figure()
    plt.plot(out)
    plt.show()

    peaks = out.astype(int)
    plt.figure()
    xx = np.linspace(0, N, N, endpoint=True)
    plt.plot(xx, grad_signal)
    plt.plot(xx[peaks], grad_signal[peaks], '*')

if not PV:
    peaks, _ = find_peaks(signal_nonlin_wl, height=height_si, distance=pedist)
    plt.figure()
    xx = np.linspace(0, N, N, endpoint=True)
    plt.plot(xx, signal_nonlin_wl)
    plt.plot(xx[peaks], signal_nonlin_wl[peaks], '*')


linpeaks = np.linspace(peaks[0], peaks[-1], len(peaks))


peak_pos_cor_interp_func = interp1d(
    peaks, linpeaks, kind=kind1, fill_value="extrapolate")
siglength = np.linspace(peaks[0],
                        peaks[-1],
                        len(signal_nonlin_wl[peaks[0]:peaks[-1]]),
                        endpoint=True)


CalVector = peak_pos_cor_interp_func(siglength)

if PF:
    # fit pol
    x = np.linspace(peaks[0], peaks[-1], len(CalVector))
    coefs = poly.polyfit(x, CalVector, deg=3)

    f = np.poly1d(coefs)

    ffit = poly.polyval(x, coefs)

    plt.figure()
    plt.plot(CalVector)
    plt.plot(ffit)

    CalVector = ffit
    plt.show()


uncorrected = abs(np.fft.fftshift(np.fft.fft(fri)))

remap_interp_func = interp1d(CalVector,
                             signal_nonlin_wl[peaks[0]:peaks[-1]],
                             kind=kind1,
                             fill_value="extrapolate")
signal_2nonlin_wl = remap_interp_func(np.linspace(
    peaks[0], peaks[-1], len(CalVector), endpoint=True))

NN = (N - len(CalVector)) / 2

signal_2nonlin_wl = np.pad(signal_2nonlin_wl, (int(NN), int(NN)), 'constant')
corrected = abs(np.fft.fftshift(np.fft.fft(signal_2nonlin_wl)))

np.save('./settings/calibration_vector.npy', CalVector)
boundaries = np.array([peaks[0], peaks[-1]])
np.save('./settings/boundaries.npy', boundaries)

plt.figure()
plt.plot(np.log10(uncorrected))
plt.plot(np.log10(corrected))
plt.show()
