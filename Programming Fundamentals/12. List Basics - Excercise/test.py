user_input = input().split()

my_list = []

for digit in user_input:
    my_list.append(digit)

new_list_int = []

for index in my_list:
    new_list_int.append(int(index))

newest_list = []

for index_2 in new_list_int:
    new_index = index_2 * 2
    newest_list.append(new_index)

for index_2 in newest_list:
    

print(newest_list)
