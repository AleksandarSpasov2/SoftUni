def main():
    rows = int(input())
    students = {}
    for student in range(rows):
        name = input()
        grade = float(input())
        if grade >= 4.5:
            students[name] = grade

    print_students(students)


def print_students(students):
    for key, value in students.items():
        print(f'{key} -> {value:.2f}')


main()