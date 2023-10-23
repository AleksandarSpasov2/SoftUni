def sum_numbers(my_list):
    total_sum = 0
    for number in my_list:
        total_sum += number
    return total_sum


new_list = [1, 2, 3]

list_sum = sum_numbers(new_list)
print(list_sum)

