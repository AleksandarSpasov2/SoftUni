items = {
    'shards': 0,
    'fragments': 0,
    'motes': 0
}

obtained = False

while not obtained:
    items_input = input().split()

    for element in range(0, len(items_input), 2):
        quantity = int(items_input[element])
        material = items_input[element + 1].lower()

        if material not in items.keys():
            items[material] = 0
        items[material] += quantity

        if items["shards"] >= 250:
            items["shards"] -= 250
            print("Shadowmourne obtained!")
            obtained = True

        elif items["fragments"] >= 250:
            items["fragments"] -= 250
            print("Valanyr obtained!")
            obtained = True

        elif items["motes"] >= 250:
            items["motes"] -= 250
            print("Dragonwrath obtained!")
            obtained = True

for key, value in items.items():
    print(f'{key}: {value}')