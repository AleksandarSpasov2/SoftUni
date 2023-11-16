resource_dict = {}
while True:
    item = input()

    if item == 'stop':
        break

    key = item
    item_2 = input()
    quantity = int(item_2)
    if key not in resource_dict:
        resource_dict[key] = quantity
    else:
        resource_dict[key] += quantity

for key, value in resource_dict.items():
    print(f'{key} -> {value}')

