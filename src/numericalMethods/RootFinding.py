"""
Búsqueda de raíces
Este módulo contiene métodos para la búsqueda de raíces de equationes de la forma f(x)=0, con f funcion real de variable real, continua y de derivada continua
"""

from sympy import *

x = Symbol ('x')

def declare_function(equation):
    global x
    return sympify(equation)

def bolzano_Gauchy(f, a, b):
    """
    Halla aplicando el teorema de Bolzano-Cauchy si existe un cero en la funcion f dentro del intervalo cerrado [a,b]

    Argumentos
    ----------

    f - Función a analizar\n
    a - Extremo inferior del intervalo\n
    b - Extremo superior del intervalo\n

    Devuelve
    --------

    Booleano - indica si se encontró o no un cero en el intervalo

    """
    return f.subs(x, a) * f.subs(x, b) < 0


def biseccion (f, a, b, tol = 1.0e-6):
    """
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
    """

    global x
    if a > b:
        raise ValueError ("Intervalo mal definido")
    if f.subs (x, a) * f.subs (x, b) >= 0.0:
        raise ValueError ("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
        raise ValueError ("La cota de error debe ser un número positivo")

    half = (a + b) / 2.0

    while True:
        if b - a < tol:
            return half
        elif f.subs (x, a) * f.subs (x, half) > 0:
            a = half
        else:
            b = half
        half = (a + b) / 2.0

def newton_rhapson(equation,x_0,es):
    """
    Halla la raíz de la función f en el entorno de x_0 mediante el método de
    Newton.

    Argumentos:
    ----------
    f - Función\n
    x_0 - Punto de partida del método\n
    es - tolerancia estimada

    Devuelve:
    ---------
    x - Raíz de la ecuación en el entorno de x_0

    Excepciones
    -----------
    RuntimeError - No hubo convergencia superado el número máximo de iteraciones
    ZeroDivisionError - La derivada se anuló en algún punto
    Exception - El valor de x se sale del dominio de definición de f
    """


    global x
    equation = declare_function (equation)
    derivate = diff (equation)
    f_NR=x-(equation/derivate)#formula de Newton Rhapson
    ea=100 #error aproximado 100%
    x_r=float(x_0)

    while ea>es:
        x_anterior=x_r
        x_r=f_NR.subs(x,x_anterior)
        if x_r !=0:
            ea=abs((x_r-x_anterior)/x_r)*100
            
    return x_r

def false_position (f, x0, x1, tol):
    """
    Halla una raíz de la función f en el intervalo [a, b] mediante el método de falsa posición.

    Argumentos\n
    f - Función, debe ser tal que f(a) f(b) &lt; 0\n
    a - Extremo inferior del intervalo\n
    b - Extremo superior del intervalo\n
    tol - Cota para el error torelable

    Devuelve
    x - Raíz de f en [a, b]
    """

    step = 1
    condition = True

    print ('\n\n*** FALSE POSITION METHOD IMPLEMENTATION ***')

    while condition:
        x2 = x0 - (x1 - x0) * f.subs (x0) / (f.subs (x1) - f.subs (x0) )
        print ('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f (x2) ) )

        if f.subs (x0) * f.subs (x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condition = abs (f.subs (x2) ) > tol

    print ('\nRequired root is: %0.8f' % x2)

def eval_poly (coefficients, value):
    """
    Evalua el polinomio coeffcients para el valor dado value

    Argumentos:\n
    coefficients - coeficientes del polinomio a evaluar\n
    value - valor a evaluar en el polinomio\n

    Devuelve:\n
    x - valor del polinomio coefficients evaluado en value
    """

    i = 1
    result = 0

    for coef in coefficients:
        result = result + coef * (value ** (len (coefficients) - i) )
        i = i + 1

    return result

def secantes (f, x0, x1, e):
    """
    Hallar la única raíz en el intervalo [x0,x1] con tolerancia e, mediante el método de las secantes\n

    Argumentos:\n
    f - función\n
    x0 - extremo inferior del intervalo\n
    x1 - extremo superior del intervalo\n
    e - tolerancia del error\n

    Devuelve:\n
    x - raíz en el intervalo [a,b]
    """

    y0 = f (x0)
    y1 = f (x1)
    xc = x1 - ( (x1 - x0) / (y1 - y0) ) * y1
    yc = f (xc)
    error = abs (xc - x1)

    if error < e:
        return xc

    return secantes (f, x1, xc, e)