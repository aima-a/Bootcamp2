''' 3.Write a function that reads content from a file and prints it. If the file does not exist, print a custom
error message. Ensure that the file is closed properly in all scenarios. '''
def content_printer(file_name):
    try:
        contents = []
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip('\n')
                contents.append(line)
        print(f'Here are the contents of your file: {contents}')
        return contents
    except FileNotFoundError:
        print(f'File {file_name} does not exist and/or was not found. Try again.')
        return None

content_printer('../Scenarios/students.txt')