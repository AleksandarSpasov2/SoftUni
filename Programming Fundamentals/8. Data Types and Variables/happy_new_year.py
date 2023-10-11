user_input = int(input())


for current_number in range(1, user_input + 1):

    current_number_as_str = str(current_number)
    index_count = 0
    is_special = False

    for index in current_number_as_str:
        index_count += int(index)

    if index_count == 5 or index_count == 7 or index_count == 11:
        is_special = True

    print(f'{current_number} -> {is_special} ')








