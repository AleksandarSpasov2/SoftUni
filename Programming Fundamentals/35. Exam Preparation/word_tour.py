def main():
    stops = input().split("::")

    command = input()
    while command != "Travel":
        command_info = command.split(":")
        action = command_info[0]

        if action == "Add Stop":
            add_stop(stops, command_info)

        elif action == "Remove Stop":
            remove_stop(stops, command_info)

        elif action == "Switch":
            switch_function(stops, command_info)

        print("::".join(stops))
        command = input()

    print(f'Ready for world tour! Planned stops: {"::".join(stops)}')


def add_stop(stops, command_info):
    index = int(command_info[1])
    string = command_info[2]
    if 0 <= index < len(stops):
        stops.insert(index, string)


def remove_stop(stops, command_info):
    start_index = int(command_info[1])
    end_index = int(command_info[2])
    if 0 <= start_index <= end_index < len(stops):
        del stops[start_index:end_index + 1]


def switch_function(stops, command_info):
    old_string = command_info[1]
    new_string = command_info[2]
    stops[:] = [new_string if stop == old_string else stop for stop in stops]


main()