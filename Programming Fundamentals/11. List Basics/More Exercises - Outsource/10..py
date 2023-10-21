def common_lists(list_1, list_2):
    common_elements = False
    for i in list_1:
        for k in list_2:
            if k == i:
                common_elements = True
    return print(common_elements)


my_list_1 = [1, 2, 4]
my_list_2 = [5]

common_lists(my_list_1, my_list_2)
