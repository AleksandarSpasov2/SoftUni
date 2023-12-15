def main():
    courses_dict = {}

    course_name_student = input().split(" : ")

    while course_name_student[0] != "end":
        course_name, student_name = course_name_student[0], course_name_student[1]
        adding_course(courses_dict, course_name, student_name)

        course_name_student = input().split(" : ")
    printing_function(courses_dict)


def adding_course(courses_dict, course_name, student_name):
    if course_name not in courses_dict:
        courses_dict[course_name] = [student_name]
    else:
        courses_dict[course_name].append(student_name)


def printing_function(course_dict):
    for key, value in course_dict.items():
        print(f'{key}: {len(value)}')
        for element in value:
            print(f'-- {element}')

main()