import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

num = [2, 20]
den = [1, 1, 2]

sys = signal.TransferFunction(num, den)

w, mag, phase = signal.bode(sys)


plt.figure()
plt.semilogx(w, mag)
plt.title('Magnitude (dB)')
plt.ylabel('Magnitude (dB)')
plt.xlabel('Frequency (Hz)')

plt.figure()
plt.semilogx(w, phase)
plt.title('Phase (deg)')
plt.ylabel('Phase (deg)')
plt.xlabel('Frequency (Hz)')

plt.show()
