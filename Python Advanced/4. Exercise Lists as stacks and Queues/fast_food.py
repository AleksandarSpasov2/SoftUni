from collections import deque

quantity_of_food = int(input())
sequence = deque(input().split())

print(max(sequence))

while sequence:
    order = sequence.popleft()
    if int(order) >= quantity_of_food:
        quantity_of_food -= int(order)
    else:
        break
if not sequence:
    print(f"Orders complete")
else:
    print(f'"Orders left: {" ".join(sequence)}')

