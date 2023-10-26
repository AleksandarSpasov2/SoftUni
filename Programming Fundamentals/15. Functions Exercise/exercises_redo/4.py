def sum_all_even_and_odd(number_input: str):
    sum_of_even = 0
    sum_of_odd = 0
    for digit in number_input:
        if int(digit) % 2 == 0:
            sum_of_even += int(digit)
        else:
            sum_of_odd += int(digit)
    return sum_of_odd, sum_of_even


number = input()
result_odd, result_even = sum_all_even_and_odd(number)
print(f'Odd sum = {result_odd}, Even sum = {result_even}')