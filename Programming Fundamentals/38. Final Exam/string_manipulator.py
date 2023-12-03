

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

    elif command == 'Lowercase':
        pass

    elif command == 'FindIndex':
        char = int(command[1])

    elif command == 'Remove':
        start_index, count = int(command[1]), int(command[2])


    command = input().split()
