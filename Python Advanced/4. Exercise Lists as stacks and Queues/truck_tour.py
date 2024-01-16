from collections import deque

truck_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

truck_data_copy = truck_data.copy()
gas_in_tank = 0
index = 0

while truck_data_copy:
    petrol, distance = truck_data_copy.popleft()

    gas_in_tank += petrol

    if gas_in_tank >= distance:
        gas_in_tank -= distance

    else:
        truck_data.rotate(-1)
        truck_data_copy = truck_data.copy()
        index += 1
        gas_in_tank = 0

print(index)