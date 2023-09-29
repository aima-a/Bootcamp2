'''Create a tuple with 5 student names.'''
my_tuple = ('Aima', 'Amna', 'Rashida', 'Ali', 'Rehman')

'''Accessing Elements: Extract the third student's name from the tuple.'''
# print(my_tuple[2])

'''Indexing: Find the index of a student's name in the tuple.'''
# print(my_tuple.index('Aima'))

'''Tuple to List: Convert a tuple into a list.'''
converted_list = list(my_tuple)
print(converted_list)

'''List to Tuple: Convert a list into a tuple.'''
my_list = [0, 1, 3, 5, 7, 9]
converted_tuple = tuple(my_list)
print(converted_tuple)

'''Tuple Unpacking: Given a tuple (x, y, z), unpack its values into three variables.'''
my_tuple_2 = ('x', 'y', 'z')
x, y, z = my_tuple_2
print(my_tuple_2)
print(x)
print(y)
print(z)
