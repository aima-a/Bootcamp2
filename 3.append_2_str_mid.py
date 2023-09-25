# Append new string in the middle of a given string
def append_2_str_mid():
    print('This function will append the second string you enter in the middle of the first string')
    str_1 = input('Please enter the first string: ')
    str_2 = input('Please enter the second string: ')
    if len(str_1) % 2 != 0:   # If string 1 is odd in length
        mid_index = len(str_1) // 2
        new_str = str_1[0:mid_index] + str_2 + str_1[mid_index:]
        return print('Your new appended string is: ' + new_str)
    else:   # If string 1 is even in length
        mid_index = len(str_1) // 2 - 1
        new_str = str_1[0:mid_index+1] + str_2 + str_1[mid_index+1:]
        return print('Your new appended string is: ' + new_str)

append_2_str_mid()
