user_input = input()

text_dict = {}

for char in user_input:
    if char != " ":
        if char not in text_dict.keys():
            text_dict[char] = 0
        text_dict[char] += 1

for key, value in text_dict.items():
    print(f'{key} -> {value}')

