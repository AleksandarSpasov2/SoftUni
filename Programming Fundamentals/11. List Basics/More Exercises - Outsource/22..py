user_input = input()


def element_find(my_list):
    is_element_found = False
    index = 0
    for i, element in enumerate(my_list):
        if element == user_input:
            is_element_found = True
            index = i

    if is_element_found:
        return print(f"Element found at index -> {index}")
    else:
        return print("Element not found")


my_list = ["a", "b", "a"]
element_find(my_list)

