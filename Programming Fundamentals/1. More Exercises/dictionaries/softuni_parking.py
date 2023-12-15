def main():
    parking_lot = {}
    cars_count = int(input())

    for car in range(cars_count):
        user_input = input().split()
        if user_input[0] == 'register':
            register_function(user_input, parking_lot)
        elif user_input[0] == 'unregister':
            unregister_function(user_input, parking_lot)

    print_function(parking_lot)


def register_function(user_input, parking_lot):
    username = user_input[1]
    license_plate = user_input[2]
    if username in parking_lot:
        print(f'ERROR: already registered with plate number {parking_lot[username]}')
    else:
        parking_lot[username] = license_plate
        print(f'{username} registered {license_plate} successfully')


def unregister_function(user_input, parking_lot):
    username = user_input[1]
    if username not in parking_lot:
        print(f'ERROR: user {username} not found')
    else:
        del parking_lot[username]
        print(f"{username} unregistered successfully")


def print_function(parking_lot):
    for key, value in parking_lot.items():
        print(f'{key} => {value}')


main()