def main():
    encrypted_message = input()

    command = input().split("|")

    while command[0] != "Decode":

        if command[0] == 'Move':


        command = input().split("|")

def move_function(command, encrypted_message):
    number_of_letters = command[1]
    first_letters = encrypted_message[:number_of_letters]
    encrypted_message = encrypted_message[number_of_letters:] + first_letters
    return encrypted_message
