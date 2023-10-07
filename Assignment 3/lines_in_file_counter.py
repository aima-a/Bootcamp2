''' 2.Write a function that takes a filename as its argument. The function should read the file and return the
number of lines in the file. If the file does not exist, it should return an appropriate error message. '''
def lines_counter(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            print(f'The number of lines in your file is {num_lines}')
            return num_lines
    except FileNotFoundError:
        print('File does not exist and/or was not found. Try again.')
        return None

lines_counter('../Scenarios/students.txt')
