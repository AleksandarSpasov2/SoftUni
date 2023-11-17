items_dict = {"shards": 0, "fragments": 0, "motes": 0}

items_input = input().split()

obtained = False

while not obtained:
    for index in range(0, len(items_input), 2):
        value = int(items_input[index])
        material = items_input[index + 1].lower()
    items_input = input().split()

