# OCT python GUI for 2D-3D scanning

Frequency domain OCT system control GUI

The GUI software is universal - the source of signal (change buffer thread GetBufferThread) and scanning should be changed.
The GUI is configured for stages are step-scanning systems.

Calibration allows to remove nonlinearities of spectral interferograms in k-space. The calibration vector is derived using an amplitude-based aproach: the fringes are postprocessed and positions of peaks are detected, evaluated and linearized. 

## Limitations

It seems that speed is a limitation because of (1) Loops speed in Python and (2) If on Windows, the min time resolution of the timer in Windows is 1 ms; therefore 1 kHz is the limiting factor.

