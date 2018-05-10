"""Bode plot problem
"""
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

gain = 1/20
zeros = np.array([-100, -20])
roots = np.roots([1, 8, 25])
poles = np.array([0, roots[0], roots[1]])

w, mag, phase = signal.bode((zeros, poles, gain), np.logspace(-1, 3))

plt.figure()
plt.semilogx(w, mag)
plt.figure()
plt.semilogx(w, phase)
plt.show()
