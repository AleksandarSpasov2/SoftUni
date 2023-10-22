def aliquot(int_input):
    is_aliquot = False
    total_sum = 0
    for numbers in range(1, int_input):
        if int_input % numbers == 0:
            total_sum += numbers

    if total_sum == int_input:
        is_aliquot = True
        return f'We have a perfect number!'
    else:
        return f"It's not so perfect."


user_input = int(input())
result = aliquot(user_input)
print(result)

