from ast import Try
import functions
import re as r

# "23x**3 + 5x**2 + 10x + 5",
# "x-x**2-1",
ejemplos = ["23x**3 + 5x**2 + 10x + 5", 
            "25x^2",
            "x-x**2-1"]

if __name__ == '__main__':
    for e in ejemplos:
        test = functions.coefficients(e)
        print(e, "\n", test)
        print('Descartes: {}'.format (functions.descartes(test)))
        if functions.find_roots(test):
            print('Lagrange: {}'.format(functions.lagrange(test)))




