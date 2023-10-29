rooms = int(input())

extra_chairs = 0
for current_room in range(1, rooms + 1):
    room_info = input().split()
    chairs = room_info[0]
    visitors = int(room_info[1])

    available_chairs = chairs.count('X')

    if available_chairs < visitors:
        needed_chairs = visitors - available_chairs
        print(f'{needed_chairs} more chairs needed in room {current_room}')
    else:
        free_chairs = available_chairs - visitors
        extra_chairs += free_chairs

if extra_chairs > 0:
    print(f'Game On, {extra_chairs} free chairs left')
