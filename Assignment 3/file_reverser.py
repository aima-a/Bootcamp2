'''1.Write a function that takes a filename as its argument. The function should read the content of the file
and write it back to the file in reverse order. If the file does not exist, print a custom error message.'''

def file_reverser(file_name):
    '''Reads the file and stores the reversed lines'''
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()  # Reads the lines of the file and stores them as the 'lines' variable
            reversed_lines = lines[::-1]
            # 'reversed_lines' is a list of strings, where each string represents a line from the file.
        '''Clears the file and appends the reversed lines, line by line'''
        with open(file_name, 'w') as file:  # Opening in write mode clears the file's contents
            for line in reversed_lines:
                file.write(line)    # file.write() expects a single string as an argument, so we must use a for loop
        print(f'File {file_name} has now been reversed, line by line.')
        return file_name
    except FileNotFoundError:
        print('File was not found and/or does not exist. Try again.')
        return None
    except Exception as e:
        print(f'An error occurred: {e}. Try again')
        return None

file_reverser('../Scenarios/students.txt')
