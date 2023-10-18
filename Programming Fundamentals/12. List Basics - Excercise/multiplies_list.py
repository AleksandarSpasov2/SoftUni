factor = int(input())
count = int(input())

new_list = []

for i in range(1, count + 1):
    variable = factor * i
    new_list.append(variable)

print(new_list)