'''Create a dictionary to store a book's title, author, and publication year'''
book = {'title': 'Kite Runner',
        'author': 'Khaled Hosseini',
        'publication_year': 2003
}
'''Extract the author's name from the dictionary'''
# print(book['author'])

'''Update the publication year to 2022.'''
# book['publication_year'] = 2022
# print(book['publication_year'])

'''Add a list of chapters to the book dictionary.'''
# list_of_chapter_nums = list(range(1,26))
# book['chapters'] = list_of_chapter_nums
# print(book['chapters'])

'''Remove the publication year from the dictionary.'''
# del book['publication_year']

''': Loop through the dictionary and print all the keys.'''
# for key in book:
#     print(key)

'''Loop and print all the values in the dictionary'''
# for value in book.values():
#     print(value)

'''Create a dictionary with numbers (1 to 5) as keys and their squares
as values'''
# num_dict = {}
# i = 1
# while i <= 5:
#     num_dict[i] = i**2
#     i += 1
# print(num_dict)

'''Merge two dictionaries into one.'''
# comb_dict = book.update(num_dict)
# print(comb_dict)

''': Create a deep copy of a dictionary using the copy module.'''
import copy
deep_copy_of_book = book.copy()
print(deep_copy_of_book)