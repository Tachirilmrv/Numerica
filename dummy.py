from numpy import *
import numpy.polynomial as pol


def biseccion_opt (a, b, f, d, tol = 1.0e-6):
    i = 1

    x1 = (a + b) / 2 - d / 2
    x2 = (a + b) / 2 + d / 2

    y1 = f (x1)
    y2 = f (x2)

    l = b - a

    print ("{}\t {:.5f}\t {:.5f}\t {:.5f}\t {:.5f}\t {:.5f}\t {:.5f}\t {:.5f}".format (i, a, b, l, x1, x2, y1, y2) )

    while l > tol:
        if y1 < y2:
            a = x1
        else:
            b = x2

        x1 = (a + b) / 2 - d / 2
        x2 = (a + b) / 2 + d / 2

        y1 = f (x1)
        y2 = f (x2)

        l = b - a
        i += 1

        print ("{}\t {:.5f}\t {:.5f}\t {:.5f}\t {:.5f}\t {:.5f}\t {:.5f}\t {:.5f}".format (i, a, b, l, x1, x2, y1, y2))

    print (f"El intervalo obtenido es: [{a}, {b}]")


a = 2
b = 2.1
f = lambda x : x * sin(x)
d = 0.0001
tol = 0.001

print ("{:<3}\t {:<7}\t {:<7}\t {:<7}\t {:<7}\t {:<7}\t {:<7}\t {:<7}".format("i", "a", "b", "l", "x1", "x2", "y1", "y2") )
print ('-' * 120)

biseccion_opt(a, b, f, d, tol)