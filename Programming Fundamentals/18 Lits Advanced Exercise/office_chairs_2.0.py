def extra_chairs(string_input):
    extra_chairs = 0
    for current_room in range(1, string_input):
        chairs, visitors = input().split()
        if len(chairs) < int(visitors):
            needed_chairs = abs(len(chairs) - int(visitors))
            extra_chairs -= needed_chairs
            return f'{needed_chairs} more chairs needed in room {current_room}'
        else:
            needed_chairs = abs(len(chairs) - int(visitors))
            extra_chairs += needed_chairs
            return f'Game On, {extra_chairs} free chairs left'


rooms = int(input())
print(extra_chairs(rooms))