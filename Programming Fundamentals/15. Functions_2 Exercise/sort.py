user_input = input().split()

user_input_str = []

for element in user_input:
    user_input_str.append(int(element))

sorted_list = sorted(user_input_str)

print(sorted_list)