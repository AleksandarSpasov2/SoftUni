def duplicate_removal(list_input):
    without_duplicates = []
    for item in list_input:
        if item not in without_duplicates:
            without_duplicates.append(item)
    return without_duplicates


my_list = ["a", "b", "a", "c"]
new_list = duplicate_removal(my_list)
print(new_list)
