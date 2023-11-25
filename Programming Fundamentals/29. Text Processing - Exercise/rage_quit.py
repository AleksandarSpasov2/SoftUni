def main():
    user_input = input()
    list_input = list_maker(user_input)
    counter = counter_function(list_input)


def list_maker(user_input):
    list_input = []
    for char in user_input:
        if char.isdigit():
            list_input.append(char)
        else:
            list_input.append(char)
    return list_input


def counter_function(list_input):
    unique_characters = set(list_input)
    return len(unique_characters)


def range_message(list_input):
    final_message = ''
    for index, value in enumerate(list_input):
        message = ''
        number = 0
        if