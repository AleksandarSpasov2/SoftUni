def main():
    student_grades = {}
    pair_of_rows = int(input())
    for student in range(pair_of_rows):
        student_name = input()
        grade = float(input())
        adding_function(student_grades, student_name, grade)
    printing_function(student_grades)


def adding_function(student_grades, student_name, grade):
    if student_name not in student_grades:
        student_grades[student_name] = [grade]
    else:
        student_grades[student_name].append(grade)


def printing_function(student_grades):
    for key, value in student_grades.items():
        if sum(value) >= 4.50:
            print(f'{key} -> {sum(value) / len(value)}')


main()
