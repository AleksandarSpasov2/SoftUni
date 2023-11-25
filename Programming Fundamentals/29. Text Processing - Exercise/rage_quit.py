def main():
    user_input = input()


def word_cycle(user_input):
    final_char = ''
    counter = 0
    for char in user_input:
        number = 0
        characters = ''
        if char.isalpha():
            characters += char
        else:
            number += int(char)
        capital_characters = capital_chars(characters)
        final_char += capital_characters * number
        counter += len(characters)
        


def capital_chars(characters):
    capital_characters = ''
    for char in characters:
        capital_characters += char.upper()
    return capital_characters
