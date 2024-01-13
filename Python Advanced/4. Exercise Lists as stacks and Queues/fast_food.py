from collections import deque

quantity_of_food = int(input())
sequence = deque(input().split())
max_value = 0


while sequence:
    order = sequence.popleft()
    if int(order) > max_value:
        max_value = int(order)

    if int(order) <= quantity_of_food:
        quantity_of_food -= int(order)
    else:
        break

print(max_value)

if not sequence:
    print(f"Orders complete")
else:
    print(f'"Orders left: {" ".join(sequence)}')

