def decrypt_message(input_list):
    final_message = []
    for word in input_list:
        if word[0].isnumeric() and word[1].isnumeric() and word[2].isnumeric():
            first_letter = chr((int(word[0]))+ int(word[1]) + int(word[2]))
            last_letter = word[3]
            middle_letters = word[:3:-1]
        else:
            first_letter = chr((int(word[0])) + int(word[1]))
            last_letter = word[2]
            middle_letters = word[:2:-1]

        second_letter = word[-1]
        new_word = first_letter + second_letter + middle_letters + last_letter
        final_message.append(new_word)
    return final_message


secret_message = input().split()
print(decrypt_message(secret_message))