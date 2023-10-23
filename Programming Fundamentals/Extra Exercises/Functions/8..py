def even_list_filter(list_input):
    filtered_list = []
    for element in list_input:
        if element % 2 == 0:
            filtered_list.append(element)
    return filtered_list


list_n = [1, 2, 3, 4, 5, 6,]
print(even_list_filter(list_n))
