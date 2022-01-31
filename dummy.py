from ast import Try
import functions
import re as r

# "23x**3 + 5x**2 + 10x + 5",
# "x-x**2-1",
ejemplos = ["x-x**2-1",
            "x^2 -9",
            "23x**3 + 5x**2 + 10x + 5", 
            "25x^2"]

if __name__ == '__main__':
    for e in ejemplos:
        test = functions.coefficients(e)
        print(e, "\n", test)
        print('Descartes positivo: {}'.format (functions.descartes(test)))
        print('Descartes negativo: {}'.format (functions.descartes(test,False)))
        print('Lagrange positivo: {}'.format(functions.lagrange(test)))
        print('Lagrange negativo: {}'.format(functions.lagrange(test, False)))




