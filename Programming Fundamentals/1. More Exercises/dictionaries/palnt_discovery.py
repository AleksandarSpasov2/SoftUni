def main():
    plants_dict = {}
    n = int(input())
    for plant_input in range(n):
        plant, rarity = input().split('<->')
        rarity = int(rarity)
        add_plant(plants_dict, plant, rarity)

    while True:
        command = input().split(":")
        if command[0] == 'Exhibition':
            break

        if command[0] == 'Rate':
            rate_function(plants_dict, command)
        elif command[0] == 'Update':
            update_function(plants_dict, command)
        elif command[0] == "Reset":
            reset_function(plants_dict, command)

    print_function(plants_dict)


def add_plant(plants_dict, plant, rarity):
    if plant not in plants_dict:
        plants_dict[plant] = {'rarity': rarity, 'rating': []}
    else:
        plants_dict[plant]['rarity'] = rarity


def rate_function(plants_dict, command):
    plant, rating = command[1].split(" - ")
    rating = int(rating)
    if plant not in plants_dict:
        plants_dict[plant] = {'rarity': 0, 'rating': [rating]}
    else:
        plants_dict[plant]['rating'].append(rating)


def update_function(plants_dict, command):
    plant, new_rarity = command[1].split(" - ")
    new_rarity = int(new_rarity)
    if plant not in plants_dict:
        plants_dict[plant] = {'rarity': new_rarity, 'rating': []}
    else:
        plants_dict[plant]['rarity'] = new_rarity


def reset_function(plants_dict, command):
    plant = command[1]
    if plant not in plants_dict:
        print('error')
    else:
        plants_dict[plant]['rating'].clear()


def print_function(plants_dict):
    print(plants_dict)


main()
