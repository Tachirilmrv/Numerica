import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial as pol

from src.complementaryMethods import Polynom



a = Polynom.poly_coefficients("5x^2-41x+7")
b = a[::-1]

p1 = pol.Polynomial (b)

x = np.linspace(3, 5, 500)
y = p1(x)

print(p1)
print(p1.deriv() )
print(min(y))

plt.plot (x, y)
plt.grid ()
plt.show ()