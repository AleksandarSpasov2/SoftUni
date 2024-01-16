data = tuple(float(x) for x in input().split())

same_number = {}

for element in data:
    if element not in same_number:
        same_number[element] = data.count(element)

for key, value in same_number.items():
    print(f'{key} - {value} times')