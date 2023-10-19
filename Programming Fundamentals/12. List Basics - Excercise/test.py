a = "a"
b = "b"
c = "2"

my_list = []

my_list.append(a)
my_list.append(b)
my_list.append(c)

my_list[0], my_list[2] = my_list[2], my_list[0]

print(my_list)