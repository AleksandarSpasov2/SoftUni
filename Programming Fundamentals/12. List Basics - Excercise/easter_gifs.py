gifts = input().split()

while True:
    command = str(input())

    if command == "No Money":
        break

    action_list = command.split()
    if len(action_list) == 2:
        action = action_list[0]
        product = action_list[1]
    elif len(action_list) == 3:
        action = action_list[0]
        product = action_list[1]
        index = action_list[2]
    else:
        action = action_list[0]

    if action == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == product:
                gifts[i] = "None"

    elif action == "Required":
        index_as_int = int(index)
        gifts[index_as_int] = product

    elif action == "JustInCase":
        gifts[-1] = product

    action_list.clear()

for k in gifts:
    if k == "None":
        gifts.remove(k)

print(gifts)



