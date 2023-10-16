n = int(input())

word = str(input())

my_list = []

for i in range(n):
    user_input = str(input())
    my_list.append(user_input)

print(my_list)

filtered_string = []

for current_string in my_list:
    if word in current_string:
        filtered_string.append(current_string)
print(filtered_string)
