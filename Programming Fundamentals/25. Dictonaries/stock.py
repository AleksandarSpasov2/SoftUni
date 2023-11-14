user_input = input().split()

stock = {}

for i in range(0, len(user_input), 2):
    key = user_input[i]
    value = user_input[i + 1]
    stock[key] = int(value)

search_for = input().split()

for item in search_for:
    if item in stock:
        print(f'We have {stock[item]} of {item} left')
    else:
        print(f"Sorry, we don't have {item}")