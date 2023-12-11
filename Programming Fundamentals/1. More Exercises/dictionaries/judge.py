user_input = input().split('->')

while True:
    if user_input[0] == 'no more time':
        break

    username, contest, points = user_input[0], user_input[1], int(user_input[2])

    user_input = input().split('->')