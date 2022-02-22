import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial as pol



a = [1, 0, 0, 0, 0]
b = a[::-1]

p1 = pol.Polynomial (b)

x = np.linspace(-10, 10, 500)
y = p1(x)

plt.plot (x, y)
plt.grid ()
plt.show ()