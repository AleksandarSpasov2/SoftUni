def main():
    rows = int(input())
    students = {}
    for _ in range(rows):
        name = input()
        grade = float(input())
        if name not in students.keys():
            students[name] = [grade]
        else:
            # students[name] += grade


    print_students(students)


def print_students(students):
    for key, value in students.items():
        print(f'{key} -> {value:.2f}')


main()