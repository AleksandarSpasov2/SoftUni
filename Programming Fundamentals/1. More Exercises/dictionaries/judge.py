user_input = input().split('->')
main_dict = {}


while True:
    if user_input[0] == 'no more time':
        break

    username, contest, points = user_input[0], user_input[1], int(user_input[2])
    if username not in main_dict.keys():
        main_dict[username] = ['contest': 0, "points": 0]


    user_input = input().split('->')