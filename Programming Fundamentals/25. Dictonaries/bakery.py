user_input = input().split()

stocks = {}

for i in range(0, len(user_input), 2):
    food = user_input[i]
    value = user_input[i + 1]
    stocks[food] = int(value)

print(stocks)
