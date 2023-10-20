factor = int(input())
count = int(input())

new_list = []

for number in range(count):
    variable = factor * number
    new_list.append(variable)

print(new_list)
