import numpy as np

OS = 10/100
Tp = 2
Ts1 = 7
Ts2 = 10

zeta = - np.log(OS) / np.sqrt(np.pi**2 + np.log(OS)**2)
theta = np.arccos(zeta)*180/np.pi
wd = np.pi / Tp
wn1 = 4 / zeta / Ts1
wn2 = 4 / zeta / Ts2

print("Zeta > %3.2f" % zeta)
print("Theta > %3.2f" % theta)
print("Wd > %3.2f" % wd)
print("Wn > %3.2f" % wn)
