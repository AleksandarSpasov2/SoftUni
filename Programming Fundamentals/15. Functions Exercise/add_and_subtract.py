def sum_numbers(num_1, num_2):
    result = num_1 + num_2
    return result


def subtract(result_1, num_3):
    subtract_result = result_1 - num_3
    return subtract_result


input_1 = int(input())
input_2 = int(input())
input_3 = int(input())

result_sum = sum_numbers(input_1, input_2)
final_result = subtract(result_sum, input_3)
print(final_result)

