# Write an iterative function iterPower(base, exp) that calculates the exponential base^exp by simply using successive
# multiplication. For example, iterPower(base, exp) should compute base^exp by multiplying base times itself exp times.
# Write such a function below.

# This function should take in two values - base can be a float or an integer; exp will be an integer ≥ 0.
# It should return one numerical value. Your code must be iterative - use of the ** operator is not allowed.

def iterPower(base,exp):
    """
    :param base: int or float
    :param exp: int >= 0
    :return: int or float, base^exp
    """
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        prod = 1
        for i in range(exp):
            prod *= base
    return prod
