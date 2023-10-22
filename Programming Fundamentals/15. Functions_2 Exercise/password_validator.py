def lenght_password(user_password):
    if not 6 <= len(user_password) <= 10:
        return f'Password must be between 6 and 10 characters'


def letters_digits_password(user_password_2):
    if not user_password_2.isalnum():
        return f'Password must consist only of letters and digits'


def digit_min_checker(user_password_3):
    digit_count = 0
    for element in user_password_3:
        if element.isdigit():
            digit_count += 1
            if digit_count < 2:
                return f'Password must have at least 2 digits'


user_input = input()

lenght_password(user_input)
letters_digits_password(user_input)
digit_min_checker(user_input)