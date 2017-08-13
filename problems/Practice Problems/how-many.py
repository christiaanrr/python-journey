# Consider the following sequence of expressions:
#
# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
#
# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')
# We want to write some simple procedures that work on dictionaries to return information.
#
# First, write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary.
# For example:
#
# >>> print(how_many(animals))
# 6

def how_many(x):
    """
    :param x: takes in a list
    :return: the sum of the number of values associated with the dictionary
    """
    total = 0
    for i in x.values():
        for e in i:
            total += 1
    return total
