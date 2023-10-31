def data_type(some_input):
    number_input = input()
    if some_input == "int":
        return int(number_input) * 2
    elif some_input == "real":
        result = int(some_input) * 1.5
        return f'{result:.2f}'
    elif some_input == "string":
        return f'${number_input}$'


user_input = input()
print(data_type(user_input))


