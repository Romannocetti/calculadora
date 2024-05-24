import math

def suma(a, b):
    """
    Función que realiza la suma de dos números.

    Args:
        a (float or int): Primer número.
        b (float or int): Segundo número.

    Returns:
        float or int: La suma de los dos números.
    """
    return a + b

def resta(a, b):
    """
    Función que realiza la resta entre dos números.

    Args:
        a (float or int): Primer número.
        b (float or int): Segundo número.

    Returns:
        float or int: La resta de a menos b.
    """
    return a - b

def division(a, b):
    """
    Función que realiza la división entre dos números.

    Args:
        a (float or int): Numerador.
        b (float or int): Denominador.

    Returns:
        float: El resultado de dividir a entre b, o un mensaje de error si b es cero.
    """
    if b == 0:
        return "No es posible dividir por cero"
    else:
        return a / b

def multiplicacion(a, b):
    """
    Función que realiza la multiplicación de dos números.

    Args:
        a (float or int): Primer número.
        b (float or int): Segundo número.

    Returns:
        float or int: El producto de los dos números.
    """
    return a * b

def factorial(n):
    """
    Función que calcula el factorial de un número entero no negativo.

    Args:
        n (int): Número entero no negativo.

    Returns:
        int: El factorial de n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
