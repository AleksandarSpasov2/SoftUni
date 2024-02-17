from collections import deque

amount_of_money = [int(x) for x in input().split()]
prices_of_food = deque([int(x) for x in input().split()])

food = 0

while amount_of_money and prices_of_food:
    current_money = amount_of_money[-1]
    current_price = prices_of_food[0]

    if current_money == current_price:
        food += 1
        amount_of_money.pop()
        prices_of_food.popleft()

    elif current_money > current_price:
        food += 1

        left_over = amount_of_money.pop() - prices_of_food.popleft()
        if amount_of_money:
            amount_of_money[-1] += left_over
        else:
            amount_of_money.append(left_over)

    elif current_money < current_price:
        amount_of_money.pop()
        prices_of_food.popleft()

if food >= 4:
    print(f"Gluttony of the day! Henry ate {food} foods.")

elif food == 0:
    print("Henry remained hungry. He will try next weekend again.")

else:
    if food == 1:
        print(f"Henry ate: {food} food.")
    else:
        print(f"Henry ate: {food} foods.")




