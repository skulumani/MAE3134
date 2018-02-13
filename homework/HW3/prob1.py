"""Script to generate some data for HW3
"""

import numpy as np
import sympy
from scipy import signal
import matplotlib.pyplot as plt

R1 = 40e3
R2 = 90e3
C = 5e-6

vin = 2
v0 = 0
t = np.linspace(0, 10)

a = (R1 + R2)/(R1*R2*C)
b = R1*C

num = [1/b]
den = [1, a]

sys = signal.TransferFunction(num, den)

time, response, _ = signal.lsim(sys, vin*np.ones_like(t), t)

rise_time = 2.2/a
settling_time = 4/a

print('Rise Time: {} s'.format(rise_time))
print('Settling Time: {} s'.format(settling_time))

# plot the response
fig, ax = plt.subplots()
ax.set_title('Low Pass Filter')
ax.plot(time, response)
plt.show()
