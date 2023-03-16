# OCT python GUI for 2D-3D scanning

Frequency domain OCT system control GUI

The GUI software is universal - the source of signal (change buffer thread GetBuff) and scanning should be changed.
The GUI is configured for time-encoded realization, i.e. Red Pitaya is the digitalization device, stages are step-scanning systems (Thorlabs,PI).

# System calibration is included (May 2022)

Calibration allows to remove nonlinearities of spectral interferograms in k-space. The calibration vector is derived using an amplitude-based aproach: the fringes are measured and positions of peaks are detected, evaluated and broaght to the linear space. 