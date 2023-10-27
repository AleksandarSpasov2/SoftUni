def sort_by_num(some_list):
    sorted_list = sorted(some_list, key=lambda x: int(x.split("-")[1]))
    return [element.split("-")[0] for element in sorted_list]


my_list = ["a-10", "b-2", "c-5"]
print(sort_by_num(my_list))