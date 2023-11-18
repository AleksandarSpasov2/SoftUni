row = int(input())
students_dict = {}

for student in range(row):
    name = input()
    grade = float(input())

    if name not in students_dict.keys():
        students_dict[name] = [grade]
    else:
        students_dict[name] += [grade]

for key, value in students_dict.items():
    average_gr = sum(value) / len(value)