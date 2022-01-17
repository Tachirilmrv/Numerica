import re as r
import math
from sympy import *


def coefs(input):
    regexp = r"(-?\d*)(x?)(?:(?:\^|\*\*)(\d))?"
    c = {}
    for coef, x, exp in r.findall(regexp, input):
        if not coef and not x:
            continue
        if x and not coef:
            coef = '1'
        if x and coef == "-":
            coef = "-1"
        if x and not exp:
            exp = '1'
        if coef and not x:
            exp = '0'
        exp = ord(exp) & 0x000F
        c[exp] = float(coef)
    grade = max(c)
    coeficientes = [0.0] * (grade + 1)
    for g, v in c.items():
        coeficientes[g] = v
    coeficientes.reverse()
    if coeficientes[0] < 0:
        coeficientes = [i * (-1) for i in coeficientes]
    return coeficientes

# Fórmula de LaGrange
def laGrange(values):
    b = max(max(values), abs(min(values)))
    k = find_k(values)
    if k == None:
        raise NameError('No tiene raices')
        return -1
    return 1 + math.pow(b / values[0], 1 / k)

def find_k(values: list) -> int:
    for i in range(len(values)):
        if values[i] < 0:
            return i

# Regla de Descartes
def descartes(values):
    value = values[0]
    count = 0
    for n in values[1:]:
        if value * n < 0:
            value = n
            count = count + 1
    return count

# "23x**3 + 5x**2 + 10x + 5",
# "x-x**2-1",
ejemplos = ["25x^2"]

if __name__ == '__main__':
    for e in ejemplos:
        test = coefs(e)
        print(e, "\n", test)
        print(descartes(test))
        print(laGrange(test))



