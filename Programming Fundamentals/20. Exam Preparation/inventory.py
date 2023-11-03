def main():
    collecting_items = input().split(", ")

    while True:
        command = input()

        if command == "Craft!":
            print(", ".join(s for s in collecting_items))
            exit()

        command_input = command.split("-")
        action = command_input[1]

        if action == "Collect":
            item = command_input[1]
            collect(item, collecting_items)

        elif action == "Drop":
            item = command_input[1]
            drop(item, collecting_items)

        elif action == "Combine Items":
            old_item, new_item = command_input[1].split(":")
            combine_items(old_item, new_item, collecting_items)

        elif action == "Renew":
            item = command_input[1]
            renew(item, collecting_items)


def renew(item, collecting_items):
    if item in collecting_items:
        collecting_items.remove(item)
        collecting_items.append(item)


def drop(item, collecting_items):
    if item in collecting_items:
        collecting_items.remove(item)


def collect(item, collecting_items):
    if item not in collecting_items:
        collecting_items.append(item)


def combine_items(old_item, new_item, collecting_items):
    if old_item in collecting_items:
        index = collecting_items.index(old_item)
        collecting_items.insert(new_item, int(index))
        collecting_items.remove(old_item)


main()



