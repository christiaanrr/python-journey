# Practice for fun!

x = -49
epsilon = 0.01
low = 0
high = x
guesses = 0
search = (high + low)/2.0

if x > 0:
    while abs(search**2 - x) >= epsilon:
        guesses += 1
        if search**2 < x:
            low = search
        else:
            high = search
        search = (high + low)/2.0

if x < 0:
    x = -x
    while abs(search**2 - x) >= epsilon:
        guesses += 1
        if search**2 < x:
            low = search
        else:
            high = search
        search = (high + low)/2.0
    x = -x
print('The square root of', x, 'is:', search)
print('It took', guesses,'amount of guesses to find the answer')