items_dict = {"shards": 0, "fragments": 0, "motes": 0}

items_input = input().split()

obtained = False

while not obtained:
    for index in range(0, len(items_input), 2):
        value = int(items_input[index])
        material = items_input[index + 1].lower()
        if material not in items_dict.keys():
            items_dict[material] = 0
        items_dict[material] += value

        if items_dict["shards"] >= 250:
            items_dict["shards"] -= 250
            print("Shadowmourne obtained!")
            obtained = True
        elif:
    items_input = input().split()

