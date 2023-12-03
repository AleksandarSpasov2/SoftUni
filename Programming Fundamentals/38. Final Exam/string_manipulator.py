

string = input()

command = input().split()
action = command[0]

while action != 'End':
    if action == 'Translate':
        char, replacement = command[1], command[2]
        string = string.replace(char, replacement)
        print(string)

    elif command == 'Includes':
        substring = command[1]
        if substring in string:
            print(f'True')
        else:
            print(f'False')

    elif command == 'Start':
        substring = command[1]
        if string.startswith(substring):
            print(f'True')
        else:
            print(f'False')

    elif command == 'Lowercase':
        string = string.lower()
        print(string)

    elif command == 'FindIndex':
        char = int(command[1])
        index = string.index(char)
        print(index)

    elif command == 'Remove':
        start_index, count = int(command[1]), int(command[2])
        string = string[:start_index] + start_index[start_index + count:]
        print(string)

    command = input().split()
