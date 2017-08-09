# Problem Set 1 Question 1
#
# Question
#
# Assume s is a string of lower case characters.
#
# Write a program that prints the number of times the string 'bob'
# occurs in s. For example, if s = 'azcbobobegghakl', then your
# program should print Number of times bob occurs is: 2

##Solution##
s = 'azcbobobegghakl'
vowels = 0

for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        vowels += 1
print('Number of vowels:', vowels)