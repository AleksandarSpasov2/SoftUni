user_input = list(input())

new_text = []

for element in range(len(user_input)):
    new_text.append(user_input.pop())

print(''.join(new_text))
