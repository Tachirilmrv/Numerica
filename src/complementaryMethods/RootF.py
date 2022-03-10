import math
from src.complementaryMethods.Polynom import positive_max_grade



def negative_interval(values):
    """
    Transforma la ecuacion para hallar los ceros del intervalo negativo

    Argumentos:
    ----------
    values - coeficientes de la ecuacion

    Devuelve:
    --------
    La lista de los coeficientes para el intervalo negativo
    """

    result = list.copy(values)

    if len(values) % 2 == 0:  # si tiene una cantidad par de coeficientes significa que el grado es impar
        i = 0
        result = positive_max_grade(values)
    else:
        i = 1

    for v in range(i, len(result) - 1, 2):
        result[v] = result[v] * (-1)

    return result


def has_roots(coef):
    """
    Devuelve True si el polinomio tiene al menos 1 raíz
    """
    return descartes(coef) != 0


def descartes(values, pos_intv = True):
    """
    Aplica la regla de descartes para hallar la mayor cantidad de raíces del polinomio

    Argumentos:
    ------------
    values - lista de los valores de los coeficientes\n
    pos_intv - boolean, True para intervalo positivo(default), false para intervalo negativo

    Devuelve:
    ----------
    Cantidad de raíces del polinomio en el intervalo dado
    """

    if not pos_intv:
        result = __aux_descartes(negative_interval(values))
    else:
        result = __aux_descartes(values)

    return result

def __aux_descartes(values):
    value = values[0]
    count = 0

    for n in values [1:]:
        if value * n < 0:
            value = n
            count = count + 1

    return count


def lagrange(values, interval = True):
    """
    Aplica la regla de lagrange para acotar la raíz de un polinomio

    Argumentos:
    ------------
    values - lista de los valores de los coeficientes\n
    interval - boolean, True para intervalo positivo(default), false para intervalo negativo

    Devuelve:
    ----------
    Valor acotado del intervalo de la raiz
    """

    if not interval:
        result = __aux_lagrange(negative_interval(values))
    else:
        result = __aux_lagrange(values)

    return result

def __aux_lagrange(values):
    b = max(max(values), abs(min(values)))
    k = __find_k(values)

    if k is None:
        return None

    return 1 + math.pow(b / values [0], 1 / k)

def __find_k(values: list) -> int:
    for i in range(len(values)):
        if values [i] < 0:
            return i