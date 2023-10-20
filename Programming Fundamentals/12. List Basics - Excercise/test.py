user_input = input().split()

mid_list = len(user_input) // 2

left_side = user_input[:mid_list]
right_side = user_input[mid_list:]
transformed_list = []

for card in range(len(left_side)):
    transformed_list.append(left_side[card])
    transformed_list.append(right_side[card])

print(transformed_list)


