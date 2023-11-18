def main():
    row = int(input())
    students_dict = {}

    for student in range(row):
        name = input()
        grade = float(input())

        if name not in students_dict.keys():
            students_dict[name] = [grade]
        else:
            students_dict[name] += [grade]

    average_garde(students_dict)
    print_function(students_dict)


def average_garde(students_dict):
    for key, value in students_dict.items():
        average_gr = sum(value) / len(value)
        if average_gr >= 4.50:
            students_dict[key] = average_gr
        else:
            del students_dict[key]


def print_function(students_dict):
    for key, value in students_dict.items():
        print(f'{key} -> {value:.2f}')

main()



