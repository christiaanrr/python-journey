def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    max = None
    numList = {}
    for number in L:
        if number not in numList:
            numList[number] = 1
        else:
            numList[number] += 1
    for each in numList:
        if each %2 != 0:
            max = each
            if max < each:
                max = each
    return max
