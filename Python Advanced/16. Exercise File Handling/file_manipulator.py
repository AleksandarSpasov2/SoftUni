import os


def create_command(info):
    file_name = info[0]
    with open(f'resources\\{file_name}', 'w'): pass


def add_command(info):
    with open(f'resources\\{info[0]}', 'a') as file:
        file.write(f'{info[1]}\n')


def replace_command(info):
    try:
        with open(f'resources\\{info[0]}', 'r+') as file:
            text = file.read()
            text = text.replace(info[1], info[2])

            file.seek(0)
            file.write(text)
            file.truncate()

    except FileNotFoundError:
        print(f'An error occurred')


def delete_command(info):
    file_name = info[0]
    try:
        os.remove(f'resources\\{file_name}')

    except FileNotFoundError:
        print(f'An error occurred')


while True:
    command, *info = input().split('-')

    if command == "End":
        break

    elif command == 'Create':
        create_command(info)

    elif command == "Add":
        add_command(info)

    elif command == "Replace":
        replace_command(info)

    elif command == 'Delete':
        delete_command(info)
