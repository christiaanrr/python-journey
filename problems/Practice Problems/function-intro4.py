# Write a Python function, isOdd, that takes in one number and returns True when the number is odd and False otherwise.
#
# You should use the % (mod) operator, not if.
#
# This function takes in one number and returns a boolean.

def isOdd(number):
    """
    :param number: an int or float
    :return: true or false if odd
    """
    return number %2 != 0
