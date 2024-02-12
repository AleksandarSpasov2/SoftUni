import os


file_name = 'numbers.txt'

path = os.path.join('resources', file_name)

with open(path) as file:
    print(file.closed)

print(file.closed)