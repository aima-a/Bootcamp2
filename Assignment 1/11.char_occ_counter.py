'''Write a program to count occurrences of all characters within a string
count_dict['key1'] = 'value1'
count_dict['key2'] = 'value2' '''

str1 = "Apple"
# Result: {'A': 1, 'p': 2, 'l': 1, 'e': 1}
def char_occ_counter(str):
    count_dict = {}
    unique_chars = {char for char in str}
    for char in unique_chars:
        count_dict[char] = str.count(char)
    return print(count_dict)

char_occ_counter(str1)
