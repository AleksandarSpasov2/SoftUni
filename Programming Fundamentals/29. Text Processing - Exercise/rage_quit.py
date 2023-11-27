def main():
    user_input = input()
    list_input = list_maker(user_input)
    unique_symbols_count = counter_function(list_input)
    rage_msg = rage_message(list_input)

    # Print the number of unique symbols
    print(f"Unique symbols used: {unique_symbols_count}")

    # Print the rage message
    print(rage_msg)


def list_maker(user_input):
    list_input = []
    for char in user_input:
        if char.isalpha():  # Only append non-numeric characters
            list_input.append(char.upper())
    return list_input


def counter_function(list_input):
    unique_characters = set(list_input)
    return len(unique_characters)


def rage_message(list_input):
    final_message = ''
    for index, value in enumerate(list_input):
        message = ''
        number = 0
        if value.isdigit():
            number = int(value)
            message = list_input[index - 1] * number
        final_message += message

    return final_message


main()
