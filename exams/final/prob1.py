import numpy as np

OS = 5/100
Tp = 1
Ts = 5

zeta = - np.log(OS) / np.sqrt(np.pi**2 + np.log(OS)**2)
theta = np.arccos(zeta)*180/np.pi
wd = np.pi / Tp
sigma = 4 / Ts
wn = 4 / zeta / Ts

print("Zeta < %3.2f" % zeta)
print("Theta > %3.2f" % theta)
print("{} < sigmad ".format(sigma))
print("{} < wn ".format(sigma/zeta))
print("wd > {}".format(wd))


