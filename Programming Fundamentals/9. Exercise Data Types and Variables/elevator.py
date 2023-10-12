number_of_people = int(input())
capacity = int(input())

course = number_of_people // capacity
if number_of_people % capacity != 0:
    course += 1

print(course)

