def list_int(user_input):
    user_input_int = []
    for num in user_input:
        user_input_int.append(int(num))
    return user_input_int


def remove_zeroes(user_input):
    counter = 0
    zeroless_list = []
    for num in user_input:
        if num == 0:
            counter += 1
        else:
            zeroless_list.append(num)
    for zero in range(counter):
        zeroless_list.append(0)
    return zeroless_list


user_input = input().split(", ")
user_input_int = list_int(user_input)
user_input_int = remove_zeroes(user_input_int)
print(user_input_int)
