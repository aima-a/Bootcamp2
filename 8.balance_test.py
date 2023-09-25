'''Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the
characters in the s1 are present in s2. The character’s position doesn’t matter.'''

s1 = "Yn"
s2 = "PYnative"
s3 = "Ynf"

def balance_test(str1, str2):
    counter = 0
    for char in str1:
        if char in str2:
            counter += 1
    if len(str1) == counter:
        print('The strings are balanced.')
    else:
        print('The strings are not balanced')

balance_test(s2, s3)
