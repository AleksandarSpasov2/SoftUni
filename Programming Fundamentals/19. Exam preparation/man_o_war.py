def main():
    status_pirate = input().split(">")
    status_warship = input().split(">")
    max_health = int(input())

    while True:
        command = input()
        if command == "Retire":
            break
        command_input = command.split()
        action = command_input[1]

        if action == "Fire":
            fire_function(status_warship, command_input)

        elif action == "Defend":


def fire_function(status_warship, command_input):
    index = int(command_input[1])
    damage = int(command_input[2])
    if index in status_warship:
        status_warship[index] -= damage
        if status_warship[index] <= 0:
            print("You won! The enemy ship has sunken.")


def defend_function(command_input, status_pirate):
    start_index = command_input[1]
    end_index = command_input[2]
    damage = command_input[3]
    if start_index in status_pirate and end_index in status_pirate:






