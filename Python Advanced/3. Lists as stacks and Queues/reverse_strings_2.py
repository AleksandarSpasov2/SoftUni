user_input = list(input())

new_text = []

for element in range(len(user_input)):
    new_letter = user_input.pop()
    new_text.append(new_letter)

print(''.join(new_text))
