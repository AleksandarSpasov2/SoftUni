def element_removal(list_1):
    new_list = []
    for i, element in enumerate(list_1):
        if i == 0 or i == 4 or i == 5:
            continue
        else:
            new_list.append(element)
    return print(new_list)


my_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

element_removal(my_list)
