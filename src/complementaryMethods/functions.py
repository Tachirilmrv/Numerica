'''
Búsqueda de raíces
Este módulo contiene métodos para la búsqueda de raíces de ecuaciones de la forma f(x)=0, con f funcion real de variable real, continua y de derivada continua
'''


import re as r
import math
import numpy as np



def coefficients (input):
    '''
    Argumento
    input - recibe un polinomio escrito de manera natural
    
    Devuelve
    Una lista de float con los coeficientes del polinomio de manera ordenada

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

    for coef, x, exp in r.findall (regexp, input):
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

        exp = ord (exp) & 0x000F
        c [exp] = float (coef)

    grade = max (c)
    coeficientes = [0.0] * (grade + 1)

    for g, v in c.items ():
        coeficientes [g] = v
    coeficientes.reverse ()

    if coeficientes [0] < 0:
        coeficientes = positive_max_grade (coeficientes)

    return coeficientes

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
    coeficientes = [i * (-1) for i in values]
    return coeficientes

def descartes (values, interval = True):
    '''
    Aplica la regla de descartes para hallar la mayor cantidad de raíces del polinomio
    
    Argumentos:
    ------------
    values - lista de los valores de los coeficientes\n
    interval - boolean, True para intervalo positivo(default), false para intervalo negativo
    
    Devuelve:
    ----------
    Cantidad de raíces del polinomio en el intervalo dado
    '''

    if not interval:
        result = aux_descartes (negative_interval (values))
    else:
        result = aux_descartes (values)

    return result

def aux_descartes (values):
    value = values [0]
    count = 0

    for n in values [1:]:
        if value * n < 0:
            value = n
            count = count + 1

    return count

def negative_interval (values):
    '''
    Transforma la ecuacion para hallar los ceros del intervalo negativo

    Argumentos:
    ----------
    values - coeficientes de la ecuacion

    Devuelve:
    --------
    La lista de los coeficientes para el intervalo negativo
    '''
    result = list.copy(values) 
    if len (values) % 2 == 0: #si tiene una cantidad par de coeficientes significa que el grado es impar
        i = 0
        result = positive_max_grade(values)
    else:
        i = 1

    for v in range (i,len (result) - 1, 2):
        result[v] = result[v] * (-1)

    return result

def lagrange(values, interval = True):
    '''
    Aplica la regla de lagrange para acotar la raíz de un polinomio
    
    Argumentos:
    ------------
    values - lista de los valores de los coeficientes\n
    interval - boolean, True para intervalo positivo(default), false para intervalo negativo
    
    Devuelve:
    ----------
    Valor acotado del intervalo de la raiz
    '''
    if not interval:
        result = aux_lagrange (negative_interval (values))
    else:
        result = aux_lagrange (values)

    return result


def aux_lagrange (values):
    b = max (max (values), abs (min (values) ) )
    k = find_k (values)

    if k == None:
        return None

    return 1 + math.pow (b / values [0], 1 / k)

def find_k (values: list) -> int:
    for i in range (len (values) ):
        if values [i] < 0:
            return i

def find_roots (coef):
    '''
    Devuelve True si el polinomio tiene al menos 1 raíz
    '''
    return descartes (coef) != 0

def biseccion (f, a, b, tol = 1.0e-6):
    '''
    Halla una raíz de la función f en el intervalo [a, b] mediante el método de bisección.

    Argumentos
    ----------

    f - Función, debe ser tal que f(a) f(b) &lt; 0\n
    a - Extremo inferior del intervalo\n
    b - Extremo superior del intervalo\n
    tol (opcional) - Cota para el error absoluto de la x

    Devuelve
    --------

    x - Raíz de f en [a, b]
    '''

    if a > b:
        raise ValueError ("Intervalo mal definido")
    if f (a) * f (b) >= 0.0:
        raise ValueError ("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
        raise ValueError ("La cota de error debe ser un número positivo")

    x = (a + b) / 2.0

    while True:
        if b - a < tol:
            return x
        elif np.sign (f (a) ) * np.sign (f (x) ) > 0:
            a = x
        else:
            b = x
        x = (a + b) / 2.0

def newton (f, df, x_0, maxiter = 50, xtol = 1.0e-6, ftol = 1.0e-6):
    '''
    Halla la raíz de la función f en el entorno de x_0 mediante el método de
    Newton.\n
    Argumentos:\n
    f - Función\n
    df - Función, debe ser la función derivada de f\n
    x_0 - Punto de partida del método\n
    maxiter (opcional) - Número máximo de iteraciones\n
    xtol (opcional) - Cota para el error relativo para la raíz\n
    ftol (opcional) - Cota para el valor de la función\n
    Devuelve:\n
    x - Raíz de la ecuación en el entorno de x_0
    Excepciones
    -----------
    RuntimeError - No hubo convergencia superado el número máximo de iteraciones
    ZeroDivisionError - La derivada se anuló en algún punto
    Exception - El valor de x se sale del dominio de definición de f
    '''

    x = float (x_0) # Se convierte a número de coma flotante
    for i in range (maxiter):
        dx = -f (x) / df (x) # ¡Aquí se puede producir una división por cero!
        # Tambin x puede haber quedado fuera del dominio
        x = x + dx
        if abs (dx / x) < xtol and abs (f (x) ) < ftol:
            return x

    raise RuntimeError ("No hubo convergencia después de {} iteraciones".format (maxiter) )

def false_position (f, x0, x1, tol):
    '''
    Halla una raíz de la función f en el intervalo [a, b] mediante el método de falsa posición.

    Argumentos\n
    f - Función, debe ser tal que f(a) f(b) &lt; 0\n
    a - Extremo inferior del intervalo\n
    b - Extremo superior del intervalo\n
    tol - Cota para el error torelable

    Devuelve
    x - Raíz de f en [a, b]
    '''

    step = 1
    condition = True

    print ('\n\n*** FALSE POSITION METHOD IMPLEMENTATION ***')

    while condition:
        x2 = x0 - (x1 - x0) * f(x0) / (f (x1) - f (x0) )
        print ('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f (x2) ) )

        if f (x0) * f (x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condition = abs (f (x2) ) > tol

    print ('\nRequired root is: %0.8f' % x2)

def eval_poly (coefficients, value):
    '''
    Evalua el polinomio coeffcients para el valor dado value

    Argumentos:\n
    coefficients - coeficientes del polinomio a evaluar\n
    value - valor a evaluar en el polinomio\n

    Devuelve:\n
    x - valor del polinomio coefficients evaluado en value
    '''

    i = 1
    result = 0

    for coef in coefficients:
        result = result + coef * (value ** (len (coefficients) - i) )
        i = i + 1

    return result

def secantes (f, x0, x1, e):
    '''
    Hallar la única raíz en el intervalo [x0,x1] con tolerancia e, mediante el método de las secantes\n

    Argumentos:\n
    f - función\n
    x0 - extremo inferior del intervalo\n
    x1 - extremo superior del intervalo\n
    e - tolerancia del error\n

    Devuelve:\n
    x - raíz en el intervalo [a,b]
    '''

    y0 = f (x0)
    y1 = f (x1)
    xc = x1 - ( (x1 - x0) / (y1 - y0) ) * y1
    yc = f (xc)
    error = abs (xc - x1)

    if error < e:
        return xc

    return secantes (f, x1, xc, e)