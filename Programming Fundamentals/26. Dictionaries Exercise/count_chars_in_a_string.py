string_input = input()

string_dict = {}

for element in string_input:
    if element != " ":
        if element in string_dict:
            string_dict[element] += 1
        else:
            string_dict[element] = len(element)

for key, value in string_dict.items():
    print(f'{key} -> {value}')

