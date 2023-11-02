def main():
    status_pirate = list(map(int, input().split(">")))
    status_warship = list(map(int, input().split(">")))
    max_health = int(input())

    while True:
        command = input()
        if command == "Retire":
            break
        command_input = command.split()
        action = command_input[0]

        if action == "Fire":
            fire_function(status_warship, command_input)

        elif action == "Defend":
            defend_function(command_input, status_pirate)

        elif action == 'Repair':
            repair_function(status_pirate, command_input, max_health)

        elif action == 'Status':
            status_function(status_pirate, max_health)
    if sum(status_pirate) == sum(status_warship):
        print(f'Pirate ship status: {sum(status_pirate)}\nWarship status: {sum(status_warship)}')
        exit()


def fire_function(status_warship, command_input):
    index = int(command_input[1])
    damage = int(command_input[2])
    if 0 <= index <= len(status_warship):
        status_warship[index] -= damage
        if status_warship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            exit()


def defend_function(command_input, status_pirate):
    start_index = int(command_input[1])
    end_index = int(command_input[2])
    damage = int(command_input[3])
    if 0 <= start_index < len(status_pirate) and 0 <= end_index < len(status_pirate):
        for i in range(start_index, end_index + 1):
            status_pirate[i] -= damage
            if status_pirate[1] <= 0:
                exit()


def repair_function(status_pirate, command_input, max_health):
    index = int(command_input[1])
    health = int(command_input[2])
    if 0 <= index < len(status_pirate):
        status_pirate[index] += health
        if status_pirate[index] > max_health:
            status_pirate[index] = max_health


def status_function(status_pirate, max_health):
    percent20 = max_health * 20 / 100
    counter = 0
    for status in status_pirate:
        if status < percent20:
            counter += 1
    print(f"{counter} sections need repair.")

main()








