def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    temp = ''
    for char in secretWord:
        for i in lettersGuessed:
            if char == i:
                temp += i
        if temp == secretWord:
            break
    if temp == secretWord:
        return True
    else:
        return False

print(isWordGuessed(secretWord = 'rllgghhff', lettersGuessed = ['r', 'g', 'l', 'h', 'e', 'f']))