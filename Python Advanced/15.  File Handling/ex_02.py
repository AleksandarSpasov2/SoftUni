import os

file_name = 'numbers.txt'

path = os.path.join('resources', file_name)

file = open(path)
total_amount = 0

for line in file.readlines():
    total_amount += int(line.strip())

print(total_amount)
file.close()
print(file.closed)