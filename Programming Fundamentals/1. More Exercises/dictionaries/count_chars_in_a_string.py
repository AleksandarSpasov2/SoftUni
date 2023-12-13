def dict_creation(text_input):
    created_dict = {}
    for char in text_input:
        if char != " ":
            if char not in created_dict.keys():
                created_dict[char] = 0
            created_dict[char] += 1
    return created_dict


def print_dict(created_dict):
    for key, value in created_dict.items():
        print(f'{key} -> {value}')


text_input = input()
main_dict = dict_creation(text_input)
print_dict(main_dict)
