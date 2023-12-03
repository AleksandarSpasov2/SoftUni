def sail_function(main_dict, town, gold, population):
    if town not in main_dict:
        main_dict[town] = {"population": 0, "gold": 0}
    main_dict[town]["population"] += population
    main_dict[town]["gold"] += gold


def events_function(command, main_dict):
    action = command[0]
    if action == 'Plunder':
        town, population, gold = command[1], int(command[2]), int(command[3])
        main_dict[town]['population'] -= population
        main_dict[town]['gold'] -= gold
        print(f'{town} plundered! {gold} gold stolen, {population} citizens killed.')
        if main_dict[town]['population'] == 0 or main_dict[town]["gold"] == 0:
            print(f'"{town} has been wiped off the map')
            main_dict[town].pop()

    elif action == 'Prosper':
        town, gold = command[1], int(command[2])
        if gold < 0:
            print(f'Gold added cannot be a negative number')
        else:
            main_dict[town]['gold'] += gold
            print(f'{gold} gold added to the city treasury. {main_dict[town]} now has {main_dict[town]["gold"]} gold.')


command = input().split('||')

main_dict = {}

while command[0] != 'Sail':
    town, population, gold = command[0], int(command[1]), int(command[2])
    sail_function(main_dict, town, gold, population)
    command = input().split('||')

command = input().split('=>')
while command[0] != 'End':
    events_function(command, main_dict)
    command = input().split('=>')

if main_dict:
    print(f'"Ahoy, Captain! There are {len(main_dict)} wealthy settlements to go to:')
    for key, value in main_dict.items():
        print(f'{key} -> Population: {value["population"]} citizens, Gold: {value["population"]} kg')

else:
    print(f'Ahoy, Captain! All targets have been plundered and destroyed!')
