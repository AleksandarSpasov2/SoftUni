from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])

counter = 0
fitted = 0
all_worms = len(worms)

while worms and holes:

    current_worm = worms[-1]
    current_hole = holes[0]

    if current_worm == current_hole:
        worms.pop()
        holes.popleft()
        counter += 1
        fitted += 1

    else:
        holes.popleft()
        worms[-1] -= 3

        if current_worm <= 0:
            worms.pop()

if counter:
    print(f"Matches: {counter}")
else:
    print(f'There are no matches.')

if not worms and fitted == all_worms:
    print(f'Every worm found a suitable hole!')
elif not worms and fitted < all_worms:
    print(f"Worms left: none")
else:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")

if not holes:
    print(f"Holes left: none")
else:
    print(f"Holes left: {', '.join(str(x) for x in holes)}")


