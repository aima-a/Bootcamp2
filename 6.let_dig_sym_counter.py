# Count all letters, digits, and special symbols from a given string
str1 = "P@#yn26at^&i5ve"
def letter_digit_symbol_counter(str):
    print('This function counts all letters, digits, and special symbols from a given string.')
    #str = input('Please enter a string: ')
    alpha_count = 0
    digit_count = 0
    symbol_count = 0
    for char in str:
        if char.isalpha():
            alpha_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1
    return print(f'Total counts of letters, digits, and symbols:\nTotal letters: {alpha_count}\nTotal digits: {digit_count}\nTotal symbols: {symbol_count}')
letter_digit_symbol_counter(str1)
