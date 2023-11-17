legendary_items = {"Shadowmourne": [250, "Shards"],
                   "Valanyr": [250, "Fragments"],
                   "Dragonwrath": [250, "Motes"]
                   }

junk_materials = {}
legendary_items_found = {}

shards = 0
fragments = 0
motes = 0

user_input = input().split()
for i in range(0, len(user_input), 2):
    material = user_input[i]
    quantity = int(user_input[i + 1])

    is_legendary_found = False

    if material == "Motes" or material == "Fragments" or material == "Shards":
        if material == "Motes":
            motes += quantity
        elif material == "Fragments":
            fragments += quantity
        elif material == "Shards":
            shards += quantity

        for element in legendary_items_found.keys():
            if element in legendary_items_found.keys():
                legendary_items_found[element] += quantity
            else:
                legendary_items_found[element] = quantity

        for key, value in legendary_items_found.items():
            if key == "Motes" and value >= 250:
                is_legendary_found = True
                break
            elif key == "Fragments" and value >= 250:
                is_legendary_found = True
                break
            elif key == "Shards" and value >= 250:
                is_legendary_found = True
                break
    else:
        if material in junk_materials.keys():
            junk_materials[material] += quantity
        else:
            junk_materials[material] = quantity

if is_legendary_found:
    if motes >= 250:
        print("Dragonwrath obtained!")
    elif fragments >= 250:
        print("Valanyr obtained!")
    elif shards >= 250:
        print("Shadowmourne obtained!")

    print(f'shards: {shards}')
    print(f'fragments: {fragments}')
    print(f'motes: {motes}')

    for key, value in junk_materials.items():
        print(f'{key}: {value}')
