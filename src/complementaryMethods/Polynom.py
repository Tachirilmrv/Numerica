import re



def poly_coefficients (raw_polynomial):
    '''
    Argumento
    raw_polynomial - recibe un polinomio escrito de manera natural

    Devuelve
    Una lista de float con los coeficientes del polinomio de manera ordenada

    Ejemplo:

    \nInput:
    23x**3 + 5x**2 + 10x + 5\n
    x-x**2-1\n
    25x^2\n

    \nOutput:
    [23.0, 5.0, 10.0, 5.0]\n
    [1.0, -1.0, 1.0]\n
    [1.0, 0.0, 0.0]\n
    '''


    regexp = r"(-?\d*)(x?)(?:(?:\^|\*\*)(\d))?"
    c = {}

    for coef, x, exp in re.findall (regexp, raw_polynomial):
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

       #exp = ord (exp) & 0x000F
        try:
            c [int (exp)] = c[int (exp)] + float (coef)
        except KeyError:
            c [int (exp)] = float (coef)

    grade = max (c)
    coefficients = [0.0] * (grade + 1)

    for g, v in c.items ():
        coefficients [g] = v
    coefficients.reverse ()

    if coefficients [0] < 0:
        coefficients = positive_max_grade (coefficients)

    return coefficients


def positive_max_grade (values):
    '''
    Transforma la ecuacion y convierte el coeficiente de mayor grado a positivo

    Argumentos:
    ----------
    values - coeficientes de la ecuacion

    Devuelve:
    --------
    Lista de los coeficientes transformados
    '''

    coefficients = [i * (-1) for i in values]

    return coefficients