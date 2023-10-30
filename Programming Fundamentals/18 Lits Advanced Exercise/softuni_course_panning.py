schedule = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break
    command_input = command.split(":")

    if command_input[0] == "Add":
        if command_input[1] not in schedule:
            schedule.append(command_input[1])

    elif command_input[0] == "Insert":
        if command_input[1] not in schedule:
            schedule.insert(int(command_input[2]), command_input[1])

    elif command_input[0] == "Remove":
        if command_input[1] in schedule:
            schedule.remove(command_input[1])

    elif command_input[0] == "Swap":
        if command_input[1] in schedule and command_input[2] in schedule:
            index1 = schedule.index(command_input[1])
            index2 = schedule.index(command_input[2])
            schedule[index1], schedule[index2] = schedule[index2], schedule[index1]

    elif command_input[0] == "Exercise":
        lesson_title = command_input[1]
        if lesson_title in schedule and f"{lesson_title}-Exercise" not in schedule:
            lesson_index = schedule.index(lesson_title)
            schedule.insert(lesson_index + 1, f"{lesson_title}-Exercise")
        elif lesson_title not in schedule:
            schedule.append(lesson_title)
            schedule.append(f"{lesson_title}-Exercise")

for idx, lesson in enumerate(schedule, 1):
    print(f"{idx}.{lesson}")



