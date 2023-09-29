# Create a string made of the first, middle, and last character
str1 = input('Please enter a string: ') # Collects user input
def first_mid_last(str):    # Defines function
    if len(str) % 2 != 0:   # If string is odd in length
        mid_index = len(str) // 2  # Stores index of middle character in an odd length string
        new_string = str[::mid_index]
        return print('The first, middle, and last characters of your string are: ' + new_string) # String slicing with step
    else:
        mid_index = len(str) // 2 - 1  # Stores index of middle character in an even length string
        new_string = str[0] + str[mid_index] + str[-1]
        return print('The first, middle, and last characters of your string are: ' + new_string)  # String concat

first_mid_last(str1)    # Calls function

