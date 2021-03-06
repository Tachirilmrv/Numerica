import numpy
import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

plt.style.use ('seaborn-poster')

x = [-1, 0, 1, 2]
y = [0.37, 1, 2.72, 7.39]
P1_coeff = [1,-1.5,.5]
P2_coeff = [0, 2,-1]
P3_coeff = [0,-.5,.5]

P1 = poly.Polynomial (P1_coeff)
P2 = poly.Polynomial (P2_coeff)
P3 = poly.Polynomial (P3_coeff)

x_new = np.arange (-1.0, 3.1, 0.1)

fig = plt.figure (figsize = (10,8))
plt.plot (x_new, P1 (x_new), 'b', label = 'P1')
plt.plot (x_new, P2 (x_new), 'r', label = 'P2')
plt.plot (x_new, P3 (x_new), 'g', label = 'P3')

plt.plot (x, np.ones (len (x)), 'ko', x, np.zeros (len (x)), 'ko')
plt.title ('Lagrange Basis Polynomials')
plt.xlabel ('x')
plt.ylabel ('y')
plt.grid ()
plt.legend ()
plt.show ()

f = lagrange (x, y)

fig = plt.figure (figsize = (10,8))
plt.plot (x_new, f (x_new), 'b', x, y, 'ro')
plt.title ('Lagrange Polynomial')
plt.grid ()
plt.xlabel ('x')
plt.ylabel ('y')
plt.show ()

print (P1)
print (P2)
print (P3)
print (f"Polinomio de LaGrange {f}")