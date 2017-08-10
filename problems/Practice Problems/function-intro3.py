# Write a Python function, fourthPower, that takes in one number and returns that value raised to the fourth power.
#
# You should use the square procedure that you defined in an earlier exercise
# (you don't need to redefine square in this box; when you call square, the grader
# will use our definition).
#
# This function takes in one number and returns one number.

def square(x):
    """
    :param x: int or float
    :return: square of x
    """
    return x**2

def fourthPower(number):
    """
    :param x: int or float number
    :return: value raised to the fourth power
    """
    return (square(square(number)))
