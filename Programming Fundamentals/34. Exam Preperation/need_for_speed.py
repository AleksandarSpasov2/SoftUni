number_of_cars = int(input())
car_dict = {}

for _ in range(number_of_cars):
    user_input = input().split("|")
    car = user_input[0]
    mileage = int(user_input[1])
    fuel = int(user_input[2])
    car_dict[car] = {'mileage': mileage, "fuel": fuel}

command = input().split(':')

while command[0] != 'Stop':
    action = command[0]

    if action == 'Drive':
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])

        if fuel <= car_dict[car]['fuel']:
            car_dict[car]['fuel'] -= fuel
            car_dict[car]['mileage'] += distance
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')

            if car_dict[car]['mileage'] >= 100000:
                del car_dict[car]
                print(f'Time to sell the {car}!')

    elif action == 'Refuel':
        car = command[1]
        fuel = int(command[2])
        available_space = 75 - car_dict[car]['fuel']

        if fuel > available_space:
            fuel = available_space

        car_dict[car]['fuel'] += fuel
        print(f"{car} refueled with {fuel} liters")

    elif action == 'Revert':
        car = command[1]
        kilometers = int(command[2])
        car_dict[car]['mileage'] -= kilometers

        if car_dict[car]['mileage'] < 10000:
            car_dict[car]['mileage'] = 10000

        print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input().split(':')

for key, value in car_dict.items():
    print(f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")
