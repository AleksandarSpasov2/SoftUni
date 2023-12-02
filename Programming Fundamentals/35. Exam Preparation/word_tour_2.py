stops = input()

command = input().split()
action = command[0]

while command != 'Travel':

    if action == "Add Stop":
        index, string = int(command[1]), command[2]
        if index in range(len(stops)):
            stops = stops[:index] + string + stops[index:]

    elif action == 'Remove Stop':
        start_index, end_index = int(command[1]), int(command[2])
        if start_index in range(len(stops)) and end_index in range(len(stops)):
            stops = stops[:start_index] + stops[end_index + 1:]

    elif action == 'Switch':
        old_string, new_string = command[1], command[2]
        if old_string in stops:
            stops.replace(old_string, new_string)
    print(stops)
    command = input().split()
print(f"Ready for world tour! Planned stops: {stops}")
