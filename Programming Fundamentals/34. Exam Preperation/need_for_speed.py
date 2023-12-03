number_of_cars = int(input())
car_dict = {}
for cars in range(number_of_cars):
    user_input = input().split("|")
    car = user_input[0]
    mileage = int(user_input[1])
    fuel = int(user_input[2])
    car_dict[car] = {'mileage': 0, "fuel": 0}

command = input().split(':')
while command[0] != 'Stop':
    action = command[0]
    if action == 'Drive':
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if fuel >= car_dict[car]['fuel']:
            car_dict[car]['fuel'] -= fuel
            car_dict[car]['mileage'] += distance
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
        else:
            print(f"Not enough fuel to make that ride")

        for key, value in car_dict.items():
            if value["mileage"] >= 100000:
                del car_dict[key]

    elif action == 'Refuel':
        car = command[1]
        fuel = int(command[2])
        for key, value in car_dict.items():
            

    elif action == 'Revert':
        car = command[1]
        kilometers = int(command[2])
