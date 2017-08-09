# Problem Set 1 Question 2
#
# Question:
#
# Assume s is a string of lower case characters.
#
# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2



##Solution##
s = 'azcbobobegghakl'
count = 0
for letter in range(len(s)):
    if s[letter] == 'b':
        if s[letter+1:letter+3] == 'ob':
            count += 1
print('Number of times bob occurs:', count)