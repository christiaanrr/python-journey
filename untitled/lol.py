def evalQuadratic(a, b, c, x):
    """
    :param a, b, c: numerical values for the coefficients of a quadratic equation
    :param x: numerical value at which to evaluate the quadratic.
    :return: value of quadratic
    """
    return a * (x ** 2) + b * x + c

evalQuadratic(2, 3, 4, 1)
