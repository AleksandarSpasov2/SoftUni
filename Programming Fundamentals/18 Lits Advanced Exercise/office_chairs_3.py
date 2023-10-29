def conference_room(count_rooms):
    extra_chairs = 0
    for current_room in range(1, count_rooms + 1):
        info_room = input().split()
        chairs = info_room[0]
        visitors = info_room[1]
        difference = len(chairs) - int(visitors)
        if difference < 0:
            print(f'{abs(difference)} more chairs needed in room {current_room}')
        extra_chairs += difference
    return extra_chairs


count_of_rooms = int(input())
total_free_chairs = conference_room(count_of_rooms)
if total_free_chairs >= 0:
    print(f'Game On, {total_free_chairs} free chairs left')