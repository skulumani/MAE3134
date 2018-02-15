"""Ship roll dynamics
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

num = [2.25]
den = [1, 0.5, 2.25]

sys = signal.TransferFunction(num, den)

time, resp = signal.step(sys)

fig, ax = plt.subplots()
ax.plot(time, resp)
plt.show()

# find poles for a specifc response
Ts = 8
Tp = 4
OS = 0.2

# calculate damping ratio and natural frequency from this
zeta = 1
