tail = str(input())
body = str(input())
head = str(input())

my_list = [tail, body, head]

my_list[0], my_list[2] = my_list[2], my_list[0]

print(my_list)