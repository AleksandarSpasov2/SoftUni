def main():
    row = int(input())
    students_dict = {}

    for student in range(row):
        name = input()
        grade = float(input())

        if name not in students_dict.keys():
            students_dict[name] = [0]
        students_dict[name] += [grade]

def average_garde(students_dict):
    for key, value in students_dict.items():
        
