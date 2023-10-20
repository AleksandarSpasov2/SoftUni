def smallest_number_list(input_list):

    for number in input_list:
        smallest_num = 0
        if number < smallest_num:
            smallest_num = number
    return smallest_num

print(smallest_number_list([1, 2, 5, 8, -1]))