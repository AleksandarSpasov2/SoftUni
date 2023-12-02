message = input()
command = input()

while True:
    tokens = command.split('|')
    action = tokens[0]

    if action == 'Move':
        number_of_letters = int(tokens[1])
        message = message[number_of_letters:] + message[:number_of_letters]
    elif action == 'Insert':
        index = int(tokens[1])
        value = tokens[2]
        message = message[:index] + value + message[index:]
    elif action == "ChangeAll":
        substring = tokens[1]
        replacement = tokens[2]
        message = message.replace(substring, replacement)
    elif action == "Decode":
        print(f'The decrypted message is: {message}')
        break

    command = input()
