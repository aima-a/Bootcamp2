# Arrange string characters such that lowercase letters should come first
#string = input("Enter a string: ")

def lower_upper_scanner(string):
    print('This function arranges a given string such that lowercase letters come before uppercase letters.')
    lower_letters = ''
    upper_letters = ''
    misc = ''
    for char in string:
        if char.islower():
            lower_letters += char
        elif char.isupper():
            upper_letters += char
        else:
            misc += char
    print('Your new string arrangement is: ' + lower_letters + upper_letters + misc)

str = 'PyNaTive'
lower_upper_scanner('PyNaTiv16e')
