def odd_and_even(int_input):
    input_as_string = str(int_input)

    even_sum = 0
    odd_sum = 0

    for number in input_as_string:
        number = int(number)

        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number
    return print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')


user_input = int(input())
odd_and_even(user_input)

