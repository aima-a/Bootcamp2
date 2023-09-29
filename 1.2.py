# Create a string made of the middle three characters
str1 = input('Please enter a string at least 5 characters long: ') # Collects user input
def mid_3(str):    # Defines function
    if len(str) % 2 != 0:   # If length of string is odd
        mid_char = len(str) // 2
        mid_3_chars = str[mid_char-1:mid_char+2]
        return print('The middle three characters of your string are: ' + mid_3_chars)
    else:   # If length of string is even
        mid_char = len(str) // 2 - 1
        mid_3_chars = str[mid_char-1:mid_char+2]
        return print('Your string is even, but the middle three characters are approximately: ' + mid_3_chars)

mid_3(str1)