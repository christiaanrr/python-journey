def isIn(str1, str2):
    """
    :param str1: takes  in a string
    :param str2: takes in a string
    :return: True if str 1 or str 2 are in each other, false otherwise
    """
    if (str1 in str2) or (str2 in str1):
        return True
    else:
        return False
