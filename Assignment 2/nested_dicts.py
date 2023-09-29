'''Create a dictionary of students. Each student (key) should have another dictionary as a value containing their age and grade.'''
students = {'Emma': {'age': 10, 'grade': 5},
            'Christa': {'age': 18, 'grade': 12},
            'Eren': {'age': 16, 'grade': 10}
            }
print(students)

'''Accessing Nested Elements: Fetch the age of a specific student.'''
print(students['Emma']['age'])

'''Updating Nested Dictionary: Update the grade of a student.'''
students['Emma']['grade'] = 6
print(students['Emma']['grade'])

'''Looping through nested dictionaries: print out each student's name along with their age and grade'''
# for key in students:
#     print(key)
#     print(students[key])
for key, value in students.items():
    print(key)
    print(value)
