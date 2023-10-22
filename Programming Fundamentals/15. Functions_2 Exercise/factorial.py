def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i

    return result


def factorial_division(number_1, number_2):
    result = number_1 / number_2
    return result


user_input_1 = int(input())
user_input_2 = int(input())

first_factorial_result = factorial(user_input_1)
second_factorial_result = factorial(user_input_2)

final_result = factorial_division(first_factorial_result, second_factorial_result)
print(f'{final_result:.2f}')
