initial_list = input().split("!")

while True:
    command_1 = input()

    if command_1 == "Go Shopping!":
        break
    command = command_1.split("!")

    if command[0] == "Urgent":
        if command[1] not in initial_list:
            initial_list.insert(0, command[1])
    elif command[0] == "Unnecessary":
        if command[1] in initial_list:
            initial_list.remove(command[1])
    elif command[0] == "Correct":
        if command[1] in initial_list:
            old_item = command[1]
            new_item = command[2]
            index = initial_list.index(old_item)
            initial_list[index] = new_item

    elif command[0] == "Rearrange":
        if command[1] in initial_list:
            initial_list.remove(command[1])
            initial_list.append(command[1])

print(", ".join(s for s in initial_list))


