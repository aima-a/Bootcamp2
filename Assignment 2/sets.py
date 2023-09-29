'''Create a set of colors: "red", "green", "blue".'''
# colors = {'red',
#           'green',
#           'blue'
# }
'''Add "yellow" to the set.'''
# colors.add('yellow')

'''Remove "red" from the set.'''
# colors.remove('red')

'''Find the union of two sets. A union contains all unique elements from both sets.'''
# set_1 = {'lemon', 'orange', 'grapefruit'}
# set_2 = {'orange', 'kiwi', 'grapes'}
# print(set_1.union(set_2))

''' Find the common elements of two sets.'''
# set_a = {1, 2, 3}
# set_b = {3, 4, 5}
# for i in set_a:
#     if i in set_b:
#         print(i)
# print(set_a.intersection(set_b))

'''Identify the difference between two sets'''
# set_a = {1, 2, 3}
# set_b = {3, 4, 5}
# first_diff = set_a.difference(set_b)
# second_diff = set_b.difference(set_a)
# print(first_diff | second_diff)

''' Check if {"red", "green"} is a subset of {"red", "green", "blue"}.'''
# set1 = {"red", "green"}
# set2 = {"red", "green", "blue"}
# if set1 <= set2:
#     print('The first set {"red", "green"} is a subset of the second set {"red", "green", "blue"}')

'''Set to List: Convert a set into a list.'''
# my_set = {"red", "green", "blue"}
# conv_list = list(my_set)
# print(type(conv_list))

'''List to Set: Convert a list into a set.'''
# my_list = ['apples', 'bananas', 3, 4]
# conv_set = set(my_list)
# print(type(conv_set))

'''Set Comprehension: Create a set of numbers divisible by 3 from 1 to 15 using set comprehension.'''
# comp_set = {i for i in range(1,16) if i % 3 == 0}
# print(comp_set)