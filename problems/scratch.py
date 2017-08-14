# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


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


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    temp = ''
    for char in secretWord:
        if char in lettersGuessed:
            temp += char
        else:
            temp += '_ '
    return temp


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    temp = alphabet.split()
    tempCopy = temp[:]
    for char in lettersGuessed:
        if char in tempCopy:
            temp.remove(char)

    return ''.join(temp)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    length = len(secretWord)
    rounds = 8
    guessedLetters = []
    print('Welcome to Hangman!')
    print('I am thinking of a word that is', length, 'letters long.')
    while rounds > 0:
        print('You have', rounds, 'guesses left.')
        print('Available letters: ' + getAvailableLetters(guessedLetters))
        guessLowerCase = input('Please guess a letter: ').lower()
        if guessLowerCase in guessedLetters:
            print(
                'Sorry, you\'ve already guessed that letter: ' + getGuessedWord(secretWord, guessedLetters)
                + '\n ----------------------------------------------------------')
        elif guessLowerCase not in guessedLetters:
            guessedLetters.append(guessLowerCase)
            if guessLowerCase in secretWord:
                print(
                    'Good guess: ' + getGuessedWord(secretWord, guessedLetters)
                    + '\n ----------------------------------------------------------')
            else:
                print(
                    'OOPS! That is not a letter in my word: ' + getGuessedWord(secretWord, guessedLetters)
                    + '\n ----------------------------------------------------------')
                rounds -= 1
            if isWordGuessed(secretWord, guessedLetters) == True:
                print ('Congratulations, you\'ve won!')
                break

    if isWordGuessed(secretWord, guessedLetters) == False:
        print('Sorry, you\'ve ran out of guesses, the word was: ' + secretWord)
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
