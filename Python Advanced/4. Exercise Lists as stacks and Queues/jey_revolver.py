from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = deque([int(x) for x in input().split()])  # back to front
locks = deque([int(x) for x in input().split()])  # front to back
intelligence = int(input())

total_price_of_bullets_used = 0

while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    total_price_of_bullets_used += bullet_price

    if current_bullet <= current_lock:
        print(f'Bang!')
    else:
        locks.appendleft(current_lock)
        print(f'Ping!')

    if not bullets:
        if locks:
            print("Reloading!")

if bullets:
    print(f"{len(bullets)} bullets left. Earned ${intelligence - total_price_of_bullets_used}")
elif not locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
