def lowe_upper_cases(string_input):
    upper_cases = 0
    lower_cases = 0
    for letter in string_input:
        if letter.isupper():
            upper_cases += 1
        else:
            lower_cases += 1
    return f'Upper Cases - {upper_cases}\n Lower Cases - {lower_cases}'


user_input = str(input())
print(lowe_upper_cases(user_input))


