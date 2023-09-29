'''Create a set of colors: "red", "green", "blue".'''
colors = {'red',
          'green',
          'blue'
}
'''Add "yellow" to the set.'''
colors.add('yellow')
'''Remove "red" from the set.'''
colors.remove('red')
'''Find the union of two sets.'''

''' Find the common elements of two sets.'''

'''Identify the difference between two sets'''

''' Check if {"red", "green"} is a subset of {"red", "green", "blue"}.'''
set1 = {"red", "green"}
set2 = {"red", "green", "blue"}
if set1 <= set2:
    print('The first set {"red", "green"} is a subset of the second set {"red", "green", "blue"}')
    