import numpy as np
from scipy import signal
import sympy

sympy.init_printing(unicode=True)

s = sympy.symbols('s', complex=False)

sIminusA = sympy.Matrix([[s + 0.038, -0.896, 0, -0.0015],
               [-0.0017, s + 0.092, 0, 0.0056],
               [-1, 0, s, 3.086],
               [0, -1, 0, s]])
A = np.array([[-0.038, 0.896, 0, 0.0015],
               [0.0017,  -0.092, 0, -0.0056],
               [1, 0, 0, -3.086],
               [0, 1, 0, 0]])
B = np.array([[-0.0075, -0.023],
               [0.0017, -0.0022],
               [0, 0],
               [0, 0]])
C= np.array([[0, 0, 1, 0],
              [0, 0, 0, 1]])
D = np.array([[0, 0],
               [0, 0]])

tf = signal.ss2tf(A, B, C, D)

tf_symbolic = sympy.simplify(C*(sIminusA**-1)*B + D)

