def data_types(user_input, second_input):
    if user_input == "int":
        result = int(second_input) * 2
        return result
    elif user_input == 'real':
        result = float(second_input) * 1.5
        return f'{result:.2f}'
    elif user_input == 'string':
        result = f'${second_input}$'
        return result


user_input = input()
second_input = input()
final_result = data_types(user_input, second_input)
print(final_result)
