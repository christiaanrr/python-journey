# Write a Python function that takes in two lists and calculates whether they are permutations of each other.
# The lists can contain both integers and strings. We define a permutation as follows:
#
# - the lists have the same number of elements
# - list elements appear the same number of times in both lists
#
# If the lists are not permutations of each other, the function returns False.
# If they are permutations of each other, the function returns a tuple consisting of the following elements:
#
# - the element occuring the most times
# - how many times that element occurs
# - the type of the element that occurs the most times
#
# If both lists are empty return the tuple (None, None, None). If more than one element occurs the
# most number of times, you can return any of them.
def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''
    if len(L1) != len(L2):
        return False
    if len(L1) == 0:
        return (None, None, None)
    max_thing = None
    max_count = 0
    dictList = {}
    for i in L1:
        dictList[i] = dictList.get(i, 0) + 1
        if dictList[i] > max_count:
            max_count += 1
            max_thing = i
    for i in L2:
        dictList[i] = dictList.get(i, 0) - 1
        if dictList[i] == -1:
            return False
        return (max_thing, max_count, type(max_thing))
