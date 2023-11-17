from collections import OrderedDict

items_input = input().split()
items_dict = OrderedDict()
shards = 0
fragments = 0
motes = 0

for i in range(0, len(items_input), 2):
    quantity = int(items_input[i])
    item_name = items_input[i + 1]
    if item_name in items_dict.keys():
        items_dict[item_name] += quantity
    else:
        items_dict[item_name] = quantity

for key, value in items_dict.items():
    if key == "shards":
        shards += value
    elif key == "fragments":
        fragments += value
    elif key == "motes":
        motes += value

if shards >= 250:
    print("Shadowmourne obtained!")
    shards -= 250
elif fragments >= 250:
    print("Valanyr obtained!")
    fragments -= 250
elif motes >= 250:
    print("Dragonwrath obtained!")
    motes -= 250

print(f"shards: {shards}")
print(f"fragments: {fragments}")
print(f"motes: {motes}")

for key, value in items_dict.items():
    if key not in {"shards", "fragments", "motes"}:
        print(f'{key}: {value}')
