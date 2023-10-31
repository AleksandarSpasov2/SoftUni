sequence_of_numbers = [int(s) for s in input().split()]


while True:
    command = input()
    if command == "end":
        break
    int_command = [int(s) for s in command.split()]
    