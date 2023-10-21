def even_numbers_removal(list_1):
    new_list = []
    for element in list_1:
        if element % 2 != 0:
            new_list.append(element)

    return print(new_list)

my_list = [2, 3, 4, 6, 8, 20, 200]

even_numbers_removal(my_list)