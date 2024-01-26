from collections import deque

chocolate = [int(x) for x in input().split(', ')]
milk = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while milkshakes != 5 or chocolate or milk:
    curr_chocolate = chocolate.pop()
    curr_milk = milk.popleft()

    if curr_milk <= 0 or curr_chocolate <= 0:
        continue

    if curr_milk == curr_chocolate:
        milkshakes += 1
    else:
        milk.append(curr_milk)
        chocolate.append(curr_chocolate - 5)

if milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")

print(f"Chocolate: {' ,'.join(str(x) for x in chocolate[::-1]) or 'empty'}")
print(f'Milk: {" ,".join(str(x) for x in milk) or "empty"}')
