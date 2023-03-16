# OCT python GUI for 2D-3D scanning

Frequency domain OCT system control GUI

The GUI software is universal - the source of signal (change buffer thread GetBufferThread) and scanning should be changed.
The GUI is configured for stages are step-scanning systems.

# System calibration is included (May 2022)

Calibration allows to remove nonlinearities of spectral interferograms in k-space. The calibration vector is derived using an amplitude-based aproach: the fringes are postprocessed and positions of peaks are detected, evaluated and linearized. 