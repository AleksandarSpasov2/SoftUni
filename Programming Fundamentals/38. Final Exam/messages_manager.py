capacity = int(input())

users_dict = {}

command = input().split("=")

while command[0] != 'Statistics':

    if command[0] == 'Add':
        username, sent, received = command[1], int(command[2]), int(command[3])
        if username not in users_dict.keys():
            users_dict[username] = {"sent": sent, 'received': received}

    elif command[0] == 'Message':
        sender, reciever = command[1], command[2]
        if sender in users_dict.keys() and reciever in users_dict.keys():
            users_dict[sender]['sent'] += 1
            users_dict[reciever]['received'] += 1
        for key, value in users_dict.items():
            if value['sent'] > 10 or value['received'] > 10:
                del key
                print(f'{sender} reached the capacity!')

    elif command[0] == 'Empty':
        username = command[1]
        if username == 'All':
            users_dict.clear()
        else:
            if username in users_dict.keys():
                del users_dict[username]
        


    command = input().split("=")
