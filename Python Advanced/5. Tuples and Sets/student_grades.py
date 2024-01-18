n = int(input())
students = {}

for _ in range(n):
    name, grade = input().split()
    grade = float(grade)

    if name not in students.keys():
        students[name] = []
    students[name].append(grade)

for key, value in students.items():
    average_grade = sum(value) / len(value)
    print(f"{key} -> {' '.join(str(x) for x in value)} (avg: {average_grade:.2f})")
