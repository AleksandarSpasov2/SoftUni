students = []

course_to_search = None

while True:
    student_info = input()

    if ":" not in student_info:
        course_to_search = student_info
        break

    name, student_id, course = student_info.split(":")
    students.append({"name": name, "student_id": student_id, "course": course})

for student in students:
    if course_to_search.startswith(student["course"][0:3]):
        print(f'{student["name"]} - {student["student_id"]}')