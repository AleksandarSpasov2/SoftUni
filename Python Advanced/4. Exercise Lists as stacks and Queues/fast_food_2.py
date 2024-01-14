from collections import deque

quantity = int(input())

orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    order = orders.popleft()

    if quantity >= order:
        quantity -= order
    else:
        print(f'Orders left:', order, *orders)
else:
    print(f'Orders complete')
    
