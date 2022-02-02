from src.numericalMethods import RootFinding

# "23x**3 + 5x**2 + 10x + 5",
# "x-x**2-1",
ejemplos = ["x-x**2-1",
            "x^2 -9",
            "23x**3 + 5x**2 + 10x + 5",
            "25x^2"]

if __name__ == '__main__':
    for e in ejemplos:
        test = RootFinding.coefficients(e)
        print(e, "\n", test)
        print('Descartes positivo: {}'.format (RootFinding.descartes(test)))
        print('Descartes negativo: {}'.format (RootFinding.descartes(test, False)))
        print('Lagrange positivo: {}'.format(RootFinding.lagrange(test)))
        print('Lagrange negativo: {}'.format(RootFinding.lagrange(test, False)))