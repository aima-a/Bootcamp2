'''Write a Python program to count the number of strings where the string length is 2 or more and the first and
last character are same from a given list of strings. '''
sample_list = ['abc', 'xyz', 'aba', '1221']
def double_checker(list):
    counter = 0
    new_list = []
    for string in list:
        if len(string) >= 2:
            counter += 1
            new_list.append(string)
    for string in new_list:
        if string[0] != string[-1]:
            counter -= 1
    return print(f'The number of strings where the string length is 2 or more and the first and last character are the same is {counter}')

double_checker(sample_list)