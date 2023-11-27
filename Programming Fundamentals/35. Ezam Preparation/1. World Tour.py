def main():
    stops = input().split("::")

    command = input()
    while command != "Travel":

        command_info = command.split(":")
        action = command_info[0]
        if action == "Add Stop":
            pass
        elif action == "Remove Stop":
            pass
        elif action == "Switch":
            pass

        command = input()


def add_stop(stops, command_info):
    index = command_info[1]
    string = command_info[2]
    if index < len(stops):
        stops.insert(index, string)
