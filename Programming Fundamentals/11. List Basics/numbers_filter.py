n = int(input())

big_list = []

for i in range(n):
    user_input = int(input())
    big_list.append(user_input)

filtered_list = []
command = str(input())

if command == "even":
    for j in big_list:
        if j % 2 == 0:
            filtered_list.append(j)

elif command == "odd":
    for j in big_list:
        if j % 2 != 0:
            filtered_list.append(j)

elif command == "negative":
    for j in big_list:
        if j < 0:
            filtered_list.append(j)

elif command == "positive":
    for j in big_list:
        if j >= 0:
            filtered_list.append(j)

print(filtered_list)