# OCT python GUI for 2D-3D scanning

GUI for controlling the OCT system in the frequency domain

The GUI software is versatile for rapid prototyping - you need to change the signal source (change the GetBufferThread buffer flow; in test it is random generator) and scanning parameters.
The GUI is set up for a stepped approach; but can be modified to continous scan if the measurement speed in python is fast enough.

## Calibration integrated
Calibration allows to eliminate nonlinearities of spectral interferograms in k-space. The calibration vector is determined using an amplitude approach: after interferogram processing, peak positions are determined, evaluated to be linearized. 

## Limitations.

The speed seems to be a limitation due to (1) the loop rate in Python and (2) If on Windows, the minimum timer time resolution in Windows is 1 ms; therefore 1 kHz seems to be a limit.