# Create a new string made of the first, middle, and last characters of each input string
s1 = 'America'
s2 = 'Japan'

#str1 = input('Please enter the first string: ')
#str2 = input('Please enter the second string: ')

def first_mid_last_2(str1, str2):
    print('This program will create a new string made of the first, middle, and last characters of each input string')
    if len(str1) % 2 != 0:  # If string 1 is odd
        str1_mid = len(str1) // 2
    else:   # If string 1 is even
        str1_mid = len(str1) // 2 - 1
    if len(str2) % 2 != 0: # If string 2 is odd
        str2_mid = len(str2) // 2
    else:
        str2_mid = len(str2) // 2 - 1
    new_str = str1[0] + str2[0] + str1[str1_mid] + str2[str2_mid] + str1[-1] + str2[-1]
    print('Your new string is: ' + new_str)

first_mid_last_2(s1,s2)
