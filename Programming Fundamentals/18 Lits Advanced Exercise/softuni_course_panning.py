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
        pass

