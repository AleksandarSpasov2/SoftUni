from collections import deque

glasses = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])

waster_water = 0

while glasses and bottles:
    current_cup = glasses.popleft()
    current_bottle = bottles.pop()

    if current_cup <= current_bottle:
        waster_water += current_bottle - current_cup

    else:
        glasses.appendleft((current_cup - current_bottle))

if glasses:
    print(f'Cups: ', *glasses)
else:
    print(f'Bottles: ', *bottles)
print(f'Wasted litters of water:{waster_water}')
