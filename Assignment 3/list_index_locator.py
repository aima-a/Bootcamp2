''' 4.Write a function that takes a list and an index as its arguments. The function should return the
element at the specified index. If the index is out of range, return a custom error message. If the
provided index isn't an integer, inform the user of the invalid input. '''

def list_index_locator(list, index):
    if type(index) != int:
        raise ValueError("Index variable must be an integer.")
    try:
        result = list[index]
        print(f'The element at the specified index is {result}')
        return result
    except ValueError:
        print(ValueError)
        return None
    except IndexError:
        print(f'The index {index} is not in the range of the list {list}. Try again.')
        return None

my_list = [0, 1, 2, 3, 4, 5]
list_index_locator(my_list, 2.5)
