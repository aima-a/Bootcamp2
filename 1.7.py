'''Create a mixed String using the following rules
Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last
char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the
result.'''

s1 = "Abc"
s2 = "Xyz"
def mixed_string(str1, str2):
    new_string = ''
    zipped = zip(str1, str2)
    for item in zipped:
        new_string += item[0]  # Add the first character from str1
        new_string += item[1]  # Add the corresponding character from str2
    new_string += str1[len(str2):]
    new_string += str2[len(str1):]
    print(new_string)
mixed_string(s1,s2)

