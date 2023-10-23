def distinct_element(list_input):
    new_list = []
    for element in list_input:
        if element not in new_list:
            new_list.append(element)

    return new_list


list_input_by_user = [1, 2, 3, 4, 5, 5, 5,]
print(distinct_element(list_input_by_user))