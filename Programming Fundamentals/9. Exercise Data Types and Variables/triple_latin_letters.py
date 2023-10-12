user_input = int(input())

for first_symbol in range(user_input):
    for second_symbol in range(user_input):
        for third_symbol in range(user_input):
            print(f'{chr(97 + first_symbol)}{chr(97 + second_symbol)}{chr(97 + third_symbol)}')

