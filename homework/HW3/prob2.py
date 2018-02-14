"""Problem 2
"""

import numpy as np
import sympy
from scipy import signal
import matplotlib.pyplot as plt

b = 0.2
mp = 0.01
mc = 1
k = 1

time = np.linspace(0,10, 100)
f = 30*np.ones_like(time)

num = [1/mc]
den = [1, b/mp, k/mp]

sys = signal.TransferFunction(num, den)

_, resp1, _ = signal.lsim(sys, f, time)
_, resp2, _ = signal.lsim(sys, f, time, X0=[0, 0.1])

# new system
sys2 = signal.TransferFunction([1/mc], [1, b/mp/10, k/mp])

_, resp3, _ = signal.lsim(sys2, f, time)

fig, ax = plt.subplots()
ax.plot(time, resp1, label='A')
ax.plot(time, resp2, label='B')
ax.plot(time, resp3, label='D')
plt.legend()
plt.show()
