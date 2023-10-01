'''1. Create a txt file with students, each with multiple scores, using write mode'''

import random
import names  # Run 'python3 -m pip install names' in terminal

# Generate a list of 10 tuples with random student names and 5 random grades per student
students = [(names.get_first_name(), [random.randint(55, 100) for _ in range(5)]) for _ in range(10)]


# _ = unused placeholder variable ('I don't care about this variable")
# The students variable is different every time the code runs
# print(students)

def write_to_file(file_name, data):
    with open(file_name, 'w') as file:
        for student in data:
            student_name = student[0]
            grades = student[1]
            grades_str = ', '.join(map(str, grades))
            file.write(f'{student_name}: {grades_str}\n')
        file.close()


write_to_file('../Scenarios/students_multi.txt', students)

'''2. Read the file data and classify it into students and scores'''


def read_file(file_name):
    student_data = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(': ')
            name = parts[0]
            scores = [int(score) for score in parts[1].split(', ')]
            student_data.append((name, scores))
        return student_data


students_multi = read_file('../Scenarios/students_multi.txt')
print(students_multi)

'''3. Find and print the average score of each student'''


def avg_score_per_student(student_data):
    avg_scores = []
    for item in student_data:  # For each student's information one by one
        name = item[0]
        grades = item[1]
        total = sum(grades)
        avg = total / len(item[1])
        student_info = (name, avg)
        avg_scores.append(student_info)
    return avg_scores


class_data = avg_score_per_student(students_multi)
print(class_data)

'''Optional: calculate the average score for the whole class'''


def avg_score_for_class(avg_data):
    class_avgs = []
    for item in avg_data:
        ind_avg = item[1]
        class_avgs.append(ind_avg)
    total = sum(class_avgs)
    class_avg = total / len(class_avgs)
    return class_avg


final_result = (avg_score_for_class(class_data))
print(final_result)
