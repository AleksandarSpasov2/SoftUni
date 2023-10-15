my_list = []

for i in range(3):
    data_input = str(input())
    my_list.append(data_input)

my_list[0], my_list[2] = my_list[2], my_list[0]

print(my_list)