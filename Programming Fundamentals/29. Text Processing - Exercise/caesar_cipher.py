def main():
    message_input = input()
    new_message = ''
    for character in message_input:
        new_character = chr(ord(character) + 3)
        new_message += new_character
    print(new_message)

main()
