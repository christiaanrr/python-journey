# Consider the following sequence of expressions:
#
# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
#
# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')
# We want to write some simple procedures that work on dictionaries to return information.
#
# This time, write a procedure, called biggest, which returns the key corresponding to the entry with the largest
# number of values associated with it. If there is more than one such entry, return any one of the matching keys.
# Example usage:

# >>> biggest(animals)
# 'd'

def biggest(x):
    """
    :param x: takes in a dictionary
    :return: the key corresponding to the entry with the largest number of values associated with it
    """
    counter = 0
    max = 0
    index = ''
    for a in x:
        for i in x.values():
            counter = 0
            for e in i:
                counter += 1
                if counter > max:
                    max = counter
        if len(x[a]) == max:
            index = a
    return index
