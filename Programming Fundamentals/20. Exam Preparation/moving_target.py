def main():
    targets = list(map(int, input().split()))

    while True:
        command = input()

        if command == "End":
            return print("|".join(str(word) for word in targets))

        command_input = command.split()
        action = command_input[0]
        index = int(command_input[1])

        if action == "Shoot":
            power = int(command_input[2])
            shoot_function(power, index, targets)

        elif action == "Add":
            value = int(command_input[2])
            add_function(value, index, targets)

        elif action == "Strike":
            radius = int(command_input[2])
            strike_function(radius, index, targets)


def shoot_function(power, index, targets):
    if 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)


def add_function(value, index, targets):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print("Invalid placement!")


def strike_function(radius, index, targets):
    index_strike = index + radius
    last_index = targets.index(targets[-1])
    if index_strike > last_index:
        print("Strike missed!")
    else:
        start_index = max(0, index - radius)
        end_index = min(len(targets) - 1, index + radius)
        for i in range(end_index, start_index - 1, -1):
            del targets[i]


main()


