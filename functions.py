import re as r
import math

def coefficients(input):
    '''
    Recibe un polinomio escrito de manera natural y devuelve una lista de float con los coeficientes ordenados segun el grado y con el de mayor grado positivo
    Ejemplo:

    \nInput:\n
    23x**3 + 5x**2 + 10x + 5\n
    x-x**2-1\n
    25x^2\n

    \nOutput:\n
    [23.0, 5.0, 10.0, 5.0]\n
    [1.0, -1.0, 1.0]\n
    [1.0, 0.0, 0.0]\n
    '''
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

def descartes(values):
    '''
    Aplica la regla de descartes para hallar la mayor cantidad de raices del polinomio
    Recibe una lista con los coeficientes
    Devuelve el numero maximo de raices
    '''
    value = values[0]
    count = 0
    for n in values[1:]:
        if value * n < 0:
            value = n
            count = count + 1
    return count

def lagrange(values):
    b = max(max(values), abs(min(values)))
    k = find_k(values)
    if k == None:
        raise NameError('No tiene raices')
    return 1 + math.pow(b / values[0], 1 / k)

def find_k(values: list) -> int:
    for i in range(len(values)):
        if values[i] < 0:
            return i

def find_roots(coef):
    '''
    Devuelve True si el polinomio tiene al menos 1 raiz
    '''
    return descartes(coef) != 0