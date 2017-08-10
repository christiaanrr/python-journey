# In this problem, you'll create a program that guesses a secret number!

# The program works as follows: you (the user) thinks of an integer between 0 (inclusive)
# and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess
# too high or too low? Using bisection search, the computer will guess the user's secret number!
# Please think of a number between 0 and 100!
# Is your secret number 50?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.
# Enter 'c' to indicate I guessed correctly. l
# Is your secret number 75?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.
# Enter 'c' to indicate I guessed correctly. l
# Is your secret number 87?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.
# Enter 'c' to indicate I guessed correctly. h
# Is your secret number 81?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.
# Enter 'c' to indicate I guessed correctly. l
# Is your secret number 84?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.
# Enter 'c' to indicate I guessed correctly. h
# Is your secret number 82?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.
# Enter 'c' to indicate I guessed correctly. l
# Is your secret number 83?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.
# Enter 'c' to indicate I guessed correctly. c
# Game over. Your secret number was: 83

low = 0
high = 100
guess = (high + low)//2
number = int(input('Please think of a number between 0 and 100!'))

while guess != number:
    print('Is your secret number ' + str(guess) + '?')
    indicate = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low." +
                     " Enter 'c' to indicate I guessed correctly.")
    if indicate == 'h':
        high = guess
    elif indicate == 'l':
        low = guess
    guess = (high + low) // 2

if guess == number:
    print('Is your secret number ' + str(guess) + '?')
    end = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low." +
                " Enter 'c' to indicate I guessed correctly.")
    if end == 'c':
        print('Game over. Your secret number was: ' + str(guess))

