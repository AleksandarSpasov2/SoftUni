def decrypt_message(input_list):
    final_message = []
    for word in input_list:
        numeric_part = ""
        letter_part = ""

        for char in word:
            if char.isnumeric():
                numeric_part += char
            else:
                letter_part += char

        first_letter = chr(int(numeric_part))
        last_letter = letter_part[0]
        second_letter = letter_part[-1]

        if len(letter_part) > 2:
            middle_letters = letter_part[1:-1]
        else:
            middle_letters = ""

        new_word = first_letter + second_letter + middle_letters + last_letter
        final_message.append(new_word)

    return ' '.join(final_message)


secret_message = input().split()
print(decrypt_message(secret_message))

