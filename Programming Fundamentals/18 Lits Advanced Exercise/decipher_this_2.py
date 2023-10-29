def decipher_this(list_input):
    final_message = []
    for word in list_input:
        letter_part = ''
        numeric_part = ''
        for element in word:
            if element.isnumeric():
                numeric_part += element
            else:
                letter_part += element

        first_letter = chr(int(numeric_part))
        if len(letter_part) = 1:
            second_letter = ''
            last_letter = ''
        else:
            second_letter = letter_part[-1]
            last_letter = letter_part[0]

        if len(letter_part) > 3:
            middle_letters = letter_part[1:-1]
        else:
            middle_letters = ''
        final_word = first_letter + second_letter + middle_letters + last_letter
        final_message.append(final_word)
    return " ".join(final_message)


user_input_message = input().split()
print(decipher_this(user_input_message))
