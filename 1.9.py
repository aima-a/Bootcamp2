'''Write a program to find all occurrences of “USA” in a given string ignoring the case.'''
str1 = "Welcome to USA. usa awesome, isn't it?"
def usa_checker(str):
    usa_count = 0
    lower = 'usa'
    upper = 'USA'
    if lower in str:
        usa_count += 1
    if upper in str:
        usa_count += 1
    return print(f'The USA count is: {usa_count}')
usa_checker(str1)