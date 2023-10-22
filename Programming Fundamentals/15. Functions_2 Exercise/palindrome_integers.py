def is_palin(string_input):
    return string_input == string_input[::-1]


user_input = input().split(", ")

for number in user_input:
    statement = is_palin(number)
    print(statement)

