from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())

toys_crafted = []

presents= {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

while materials and magic_level:
    curr_material = materials.pop() if magic_level[0] or not materials[-1] else 0
    curr_magic = magic_level.popleft() if materials or not magic_level[0] else 0

    if not magic_level:
        continue

    result = curr_magic * curr_material

    if result <= 0:
        materials.append(curr_magic + curr_material)

    elif result > 0:
        if presents.get(result):
            toys_crafted.append(presents[result])

        else:
            curr_material += 15
            materials.append(curr_material)

if {"Doll", "Wooden train"}.issubset(toys_crafted) or {'Teddy bear', 'Bicycle'}.issubset(toys_crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f'"Materials left: {" ".join(str(x) for x in materials[::-1])}')

if magic_level:
    print(f'"Magic left: {" ".join(str(x) for x in magic_level)}')

print(f'{toy}: {toys_crafted.count(toy)}'for toy in sorted(set(toys_crafted)))