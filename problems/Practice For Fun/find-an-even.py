def findAnEven(L):
    """
    :param L: list of integers
    :return: first even number in L, raises valueError if no even number
    """
    for number in L:
        if number % 2 == 0:
            return number
        raise ValueError('No even number in list')
