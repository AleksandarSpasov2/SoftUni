rooms = int(input())

extra_chairs = 0
for current_room in range(1, rooms + 1):
    chairs, visitors = input().split()

    if len(chairs) < int(visitors):
        needed_chairs = abs(len(chairs) - int(visitors))
        extra_chairs -= needed_chairs
        print(f'{needed_chairs} more chairs needed in room {current_room}')
    else:
        needed_chairs = abs(len(chairs) - int(visitors))
        extra_chairs += needed_chairs

if extra_chairs > 0:
    print(f'Game On, {extra_chairs} free chairs left')





