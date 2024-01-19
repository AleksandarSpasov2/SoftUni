from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

command = input()

lane = deque()

while command != 'END':
    if command != 'green':
        lane.append(command)
    else:
        current_green = green_light_duration
        current_free = free_window_duration
        current_car = lane.popleft()
        total_duration = green_light_duration + free_window_duration
        if len(current_car) > green_light_duration:
            character_hit = len(current_car) - total_duration
            print(f"A crash happened!")
            print(f"{current_car} was hit at {character_hit - len(current_car)}.")
            break
        else:
            current_green = len(current_car) - green_light_duration
            if current_green < 0:
                current_free = free_window_duration + current_green
                current_green = 0

    command = input()