products = {}
user_input = input()
while True:

    if user_input == 'statistics':
        break
    user_input = input().split(": ")
    product = user_input[0]
    quantity = int(user_input[1])

    if product not in products:
        products[product] = 0
    products[product] += quantity