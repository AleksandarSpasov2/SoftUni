capacity = int(input())

users_dict = {}

command = input().split("=")

while command[0] != 'Statistics':

    if command[0] == 'Add':
        username, sent, received = command[1], int(command[2]), int(command[3])
        if username not in users_dict:
            users_dict[username] = {"sent": sent, 'received': received}

    elif command[0] == 'Message':
        sender, receiver = command[1], command[2]
        if sender in users_dict and receiver in users_dict:
            users_dict[sender]['sent'] += 1
            users_dict[receiver]['received'] += 1

            for user in [sender, receiver]:
                if users_dict[user]['sent'] + users_dict[user]['received'] >= capacity:
                    print(f'{user} reached the capacity!')
                    del users_dict[user]
                    break

    elif command[0] == 'Empty':
        username = command[1]
        if username == 'All':
            users_dict.clear()
        else:
            if username in users_dict:
                del users_dict[username]

    command = input().split("=")

print(f'Users count: {len(users_dict)}')
for key, value in users_dict.items():
    number_of_messages = value['sent'] + value['received']
    print(f'{key} - {number_of_messages}')
