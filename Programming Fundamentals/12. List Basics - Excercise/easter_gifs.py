gifts = input().split()


while True:
    command = str(input())

    if command == "No Money":
        break

    tokens = command.split()
    action = tokens[0]

    