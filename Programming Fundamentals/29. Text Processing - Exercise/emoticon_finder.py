text_input = input()
for character in range(len(text_input)):
    if text_input[character] == ':':
        print(f'{text_input[character]}{text_input[character + 1]}')
