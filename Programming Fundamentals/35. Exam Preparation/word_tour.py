def main():
    stops = input().split("::")

    command = input()
    while command != "Travel":

        command_info = command.split(":")
        action = command_info[0]
        if action == "Add Stop":
            add_stop(stops, command_info)
            print(stops)

        elif action == "Remove Stop":
            remove_stop(stops, command_info)
            print(stops)

        elif action == "Switch":
            switch_function(stops, command_info)
            print(f'Ready for world tour! Planned stops: {stops}')

        command = input()


def add_stop(stops, command_info):
    index = int(command_info[1])
    string = command_info[2]
    if index < len(stops):
        stops.insert(index, string)


def remove_stop(stops, command_info):
    start_index = int(command_info[1])
    end_index = int(command_info[2])
    if len(stops) - start_index >= 0 and len(stops) - end_index >= 0:
        for stop in range(stops[start_index], stops[end_index] + 1):
            stops.pop(stop)


def switch_function(stops, command_info):
    old_string = command_info[1]
    new_string = command_info[2]
    if old_string in stops:
        for index, value in enumerate(stops):
            if value == old_string:
                stops.insert(index, new_string)
                stops.pop(value)

main()