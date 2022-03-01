import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial as pol



a = [1, 2, 3, 4, 5]
#b = a[::-1]

p1 = pol.Polynomial (a)

x = np.linspace(-10, 10, 500)
y = p1(x)

print(p1)
print(p1.deriv())

plt.plot (x, y)
plt.grid ()
plt.show ()