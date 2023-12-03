string = input()

command = input().split()
action = command[0]

while action != 'End':
    if action == 'Translate':
        char, replacement = command[1], command[2]
        string = string.replace(char, replacement)
        print(string)

    elif command[0] == 'Includes':
        substring = command[1]
        if substring in string:
            print(f'True')
        else:
            print(f'False')

    elif command[0] == 'Start':
        substring = command[1]
        if string.startswith(substring):
            print(f'True')
        else:
            print(f'False')

    elif command[0] == 'Lowercase':
        string = string.lower()
        print(string)

    elif command[0] == 'FindIndex':
        char = command[1]
        index = string.index(char)
        print(index)

    elif command[0] == 'Remove':
        start_index, count = int(command[1]), int(command[2])
        string = string[:start_index] + string[start_index + count:]
        print(string)

    command = input().split()
    action = command[0]
