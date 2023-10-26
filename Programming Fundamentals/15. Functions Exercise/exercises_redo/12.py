def factorial(number):
    final_sum = 1
    for num in range(1, number + 1):
        final_sum *= num
    return final_sum


first_number_input = int(input())
second_number_input = int(input())

result = factorial(first_number_input) / factorial(second_number_input)
print(f'{result:.2f}')
