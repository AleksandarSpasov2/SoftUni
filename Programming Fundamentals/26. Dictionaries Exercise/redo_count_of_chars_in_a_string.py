def main():
    string_input = input()
    string_dict = {}
    string_cycle(string_input, string_dict)
    print_dict(string_dict)


def string_cycle(string_input, string_dict):
    for element in string_input:
        if element != " ":
            if element in string_dict:
                string_dict[element] += 1
            else:
                string_dict[element] = 1


def print_dict(string_dict):
    for key, value in string_dict.items():
        print(f'{key} -> {value}')

main()