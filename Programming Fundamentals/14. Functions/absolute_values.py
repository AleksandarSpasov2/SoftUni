user_input = list(map(float, input().split()))


def absolute_value(user_input_list):
    abs_list = []
    for number in user_input_list:
        abs_list.append(abs(number))
    return abs_list


abs_final = absolute_value(user_input)
print(abs_final)
