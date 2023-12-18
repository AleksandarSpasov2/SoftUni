import re

user_input = input()
final_list = []

while user_input:
    pattern = r'\d+'
    match = re.findall(pattern, user_input)
    if match:
        final_list.append(match)
    user_input = input()

print(final_list)
