from collections import deque

chocolates = deque(int(x) for x in input().split(', '))
milk = deque(int(x) for x in input().split(', '))

total_milkshakes = 0

while total_milkshakes != 5:
    current_chocolate = 0  # Initialize current_chocolate
    current_milk = 0
    if not chocolates or not milk:
        break
    if chocolates:
        current_chocolate = chocolates.pop()
    if milk:
        current_milk = milk.popleft()

    if current_chocolate == current_milk:
        total_milkshakes += 1
        chocolates.pop()
        milk.popleft()
        continue
    else:
        if current_chocolate <= 0:
            chocolates.pop()
            continue
        if current_milk <= 0:
            milk.popleft()
            continue

        milk.append(current_milk)
        current_chocolate -= 5
        chocolates.append(current_chocolate)

if total_milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f'Chocolate: {", ".join(map(str, chocolates))}')
else:
    print("Chocolate: empty")

if milk:
    print(f'Milk: {", ".join(map(str, milk))}')
else:
    print("Milk: empty")
