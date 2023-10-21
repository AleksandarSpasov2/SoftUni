def empty_list_checker(my_list):
    is_list_empty = False
    empty_list = []
    if my_list == empty_list:
        is_list_empty = True
    return print(is_list_empty)


my_list = [1]
empty_list_checker(my_list)
