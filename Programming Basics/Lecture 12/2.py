


bad_grades_limit = int(input())

sum_grades = 0
counter = 0
last_problem = " "
bad_grades_count = 0

while True:
    name_task = str(input())
    if name_task == "Enough":
        print(f'Average score: {sum_grades / counter:.2f}')
        print(f'Number of problems: {counter}')
        print(f'Last problem: {last_problem}')
        break

    current_grade = int(input())

    counter += 1
    sum_grades += current_grade
    last_problem = name_task

    if current_grade <= 4:
        bad_grades_count += 1
        if bad_grades_count == bad_grades_limit:
            print(f'You need a break, {bad_grades_count} poor grades.')
            break
    continue




