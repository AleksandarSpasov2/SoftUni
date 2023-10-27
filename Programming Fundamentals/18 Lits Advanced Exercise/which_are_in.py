first_list = input().split(", ")
second_list = input().split(", ")

substrings = []

for element_string_1 in first_list:
    for element_string_2 in second_list:
        if element_string_1 in element_string_2:
            substrings.append(element_string_1)
            break

print(substrings)