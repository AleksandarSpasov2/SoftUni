user_input = input()

new_string = []

for element in range(len(user_input) -1, -1, -1):
    new_string.append(user_input[element])

print(''.join(new_string))
    

