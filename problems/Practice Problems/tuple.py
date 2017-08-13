# Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output,
# where every other element of the input tuple is copied, starting with the first one.
# So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on
# this input would return the tuple ('I', 'a', 'tuple').

def oddTuples(aTuple):
    """
    :param aTuple: a tuple
    :return: a new tuple, every other element is copied
    """
    newTuple = ()
    for i in range (len(aTuple)):
        if (i % 2 == 0):
            newTuple += (aTuple[i],)

    return newTuple


print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))