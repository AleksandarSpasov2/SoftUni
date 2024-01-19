import sys
from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

command = input()

lane = deque()
total_cars_passed = 0

while True:
    if command == "END":
        print("Everyone is safe.")
        print(f"{total_cars_passed} total cars passed the crossroads.")
        break

    elif command == 'green':
        current_green = green_light_duration
        current_free = free_window_duration
        while lane:
            current_car = lane.popleft()
            if len(current_car) <= current_green:
                current_green -= len(current_car)
                total_cars_passed += 1
            else:
                current_time = len(current_car) - (len(current_car) - current_green)
                current_free -= current_time
                character_hit = len(current_car) - current_time
                if current_free < 0:
                    print("A crash happened!")
                    print(f"{current_car} was hit at {current_car[-character_hit:]}.")
                    sys.exit()
                else:
                    continue

    else:
        lane.append(command)

    command = input()
