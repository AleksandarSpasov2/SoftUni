legendary_items = {"Shadowmourne": [250, "Shards"],
                   "Valanyr": [250, "Fragments"],
                   "Dragonwrath": [250, "Motes"]
                   }

junk_materials = {}
legendary_items_found = {}

shards = 0
fragments = 0
motes = 0

quantity, material = input().split()
is_legendary_found = False

if material == "Shadowmourne" or material == "Valanyr" or material == "Dragonwrath":
    if material in legendary_items.keys():
        legendary_items_found[material] += int(quantity)
        for quantity_legend in legendary_items_found.values():
            if quantity_legend >= 250:
                is_legendary_found = True
                break
    else:
        legendary_items_found[material] = int(quantity)
        for quantity_legend in legendary_items_found.values():
            if quantity_legend >= 250:
                is_legendary_found = True
                break
else:
    if material not in junk_materials.keys():
        junk_materials[material] = int(quantity)
    else:
        junk_materials[material] += int(quantity)




