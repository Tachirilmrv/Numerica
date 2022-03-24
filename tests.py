import pytest
import sympy as sp

from src.complementaryMethods import RootF, Polynom
from src.numericalMethods import RootFinding as rf


class TestCase:

    @pytest.mark.parametrize("example", ["x-x**2-1", "x^2 -9",
                                         "23x**3 + 5x**2 + 10x + 5",
                                         "25x^2"])
    def test_polys(self, example):
        test = Polynom.poly_coefficients(example)
        

        print(example, "\n", test)
        print('Descartes positivo: {}'.format(RootF.descartes(test)))
        print('Descartes negativo: {}'.format(RootF.descartes(test, False)))
        print('Lagrange positivo: {}'.format(RootF.lagrange(test)))
        print('Lagrange negativo: {}'.format(RootF.lagrange(test, False)))

        # true if no error occurred
        assert True

    # may change the name
    def test_another_test(self):
        x = sp.Symbol('x')

        ts = rf.declare_function('x**3 + 1')

        print(ts)

        aux = rf.newton_rhapson(ts, -3, 3)
        print(aux)

        # true if no error occurred
        assert True
