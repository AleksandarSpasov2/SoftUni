def multiply_list(my_list):
    total_mul = 1
    for number in my_list:
        total_mul *= number
    return total_mul


new_list = [2, 4]

print(multiply_list(new_list))

