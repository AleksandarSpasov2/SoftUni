def main():
    students = {}
    command = input()

    while command != "exam finished":
        command_info = command.split("-")
        username = command_info[0]

        if command_info[1] == "banned":
            if username in students.keys():
                del students[username]
                continue #-------------------------------------

        language = command_info[1]
        points = int(command_info[2])

        if username not in students.keys():
            students[username] = []
        students[username].append(language)
        students[username].append(points)



def print_function(students):
    for key, value in students.items():
        print(f'{key} | {value[1]}')












