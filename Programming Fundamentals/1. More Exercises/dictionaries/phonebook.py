main_dict = {}

user_input = input()

while True:
    if "-" not in user_input:
        n = int(user_input)
        break
    tokens = user_input.split('-')
    person, number = tokens[0], tokens[1]
    if person not in main_dict.keys():
        main_dict[person] = number
    else:
        main_dict[person] = number

    user_input = input()

for _ in range(n):
    name = input()
    if name in main_dict.keys():
        print(f'{name} -> {main_dict[name]}')
    else:
        print(f'Contact {name} does not exist.')