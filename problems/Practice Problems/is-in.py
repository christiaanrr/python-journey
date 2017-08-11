# We can use the idea of bisection search to determine if a character is in a string,
# so long as the string is sorted in alphabetical order.
#
# First, test the middle character of a string against the character you're looking for (the "test character").
# If they are the same, we are done - we've found the character we're looking for!
#
# If they're not the same, check if the test character is "smaller" than the middle character.
# If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string.
# (Note that you can compare characters using Python's < function.)

# Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr.
# char will be a single character and aStr will be a string that is in alphabetical order.
# The function should return a boolean value.

# As you design the function, think very carefully about what the base cases should be.

def isIn(char, aStr):
    """
    :param char: a single character
    :param aStr: an alphabetized string
    :return: True if char is in aStr; False otherwise
    """
    if aStr == '' and char != '':
        return False

    letter = aStr[len(aStr)//2]

    if len(aStr) == 1 and char != letter or len(aStr) == 0 and char != letter:
        return False

    if char == letter:
        return True
    elif char != letter:
        if char < letter:
            aStr = aStr[0:(len(aStr)//2)]
            return isIn(char, aStr)
        elif char > letter:
            aStr = aStr[(len(aStr)//2):(len(aStr))]
            return isIn(char, aStr)
