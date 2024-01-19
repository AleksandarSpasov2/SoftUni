parking_lot = set()

for car in range(int(input())):
    direction, car_number = input().split(', ')
    if direction == "IN":
        parking_lot.add(car_number)
    elif direction == "OUT":
        if car_number in parking_lot:
            parking_lot.remove(car_number)

if parking_lot:
    for c in parking_lot:
        print(c)
else:
    print(f'Parking Lot is Empty')
