def password_validator(str_input: str):
    errors_list = []
    if len(str_input) < 6 or len(str_input) > 10:
        errors_list.append('Password must be between 6 and 10 characters')
    if not str_input.isalnum():
        errors_list.append('Password must be between 6 and 10 characters')
    digit_counter = 0
    for digit in str_input:
        if digit.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        errors_list.append('Password must have at least 2 digits')

    return errors_list


password_input = str(input())
result = password_validator(password_input)

if len(result) == 0:
    print(f'Password is valid')
else:
    print("\n".join(result))