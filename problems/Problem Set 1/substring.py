# Problem Set 1 Question 3
#
# Question:
#
# Write a program that prints the longest substring of s in which the letters
# occur in alphabetical order. For example, if s = 'azcbobobegghakl', then
# your program should print: Longest substring in alphabetical order is: beggh
#
# In the case of ties, print the first substring. For example, if s = 'abcbcd',
# then your program should print: Longest substring in alphabetical order is: abc


## Solution ##
s = 'azcbobobegghakl'
# longest substring that is alphabetically ordered (makes sure atleast first letter is printed)
longest= s[0]
# temporary substring which holds the value of alphabetical ordered string
substr = s[0]

# loop by comparing letters of substr to the letters of s, if bigger than last letter, append to substr
for i in range(1,len(s)):
    if s[i] >= substr[-1]:
        substr += s[i]
        if len(substr) > len(longest):
            longest = substr
    else:
        substr = s[i]
print(longest)