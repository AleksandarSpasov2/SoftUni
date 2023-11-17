def main():
    course_dict = {}
    while True:

        command = input()
        if command == "end":
            break
        name, student = command.split(":")
        if name not in course_dict.keys():
            course_dict[name] = [student]
        else:
            course_dict[name].append(student)

    print_dict(course_dict)


def print_dict(course_dict):
    for key, value in course_dict.items():
        print(f'{key}:{len(value)}')
        for student in value:
            print(f'--{student}')


main()

