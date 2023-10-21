def rounding_func(user_input):
    rounded_elements = []
    for element in user_input:
        rounded_elements.append(round(element))
    return print(rounded_elements)


num = input()
num_list = num.split()

num_list_int = []
for element_num in num_list:
    num_list_int.append(float(element_num))

rounding_func(num_list_int)

