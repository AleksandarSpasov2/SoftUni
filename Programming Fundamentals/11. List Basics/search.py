n = int(input())

magic_word = str(input())

my_list = []

for i in range(n):
    string = str(input())
    my_list.append(string)

print(my_list)

filtered_string = []

for j in my_list:
    if magic_word in j:
        filtered_string.append(j)
print(filtered_string)

