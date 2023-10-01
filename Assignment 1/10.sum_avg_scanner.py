'''Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all
other characters.'''
str1 = "PYnative29@#8496"
def sum_avg_scanner(str):
    digits = ''
    sum = 0
    for char in str:
        if char.isdigit():
            digits += char
    for digit in digits:
        digit_int = int(digit)
        sum += digit_int
    avg = sum / len(digits)
    print(f'The sum of the digits is {sum} and the average of the digits is {avg}')

sum_avg_scanner(str1)
