def product_calculator(product_i, quantity):
    if product_i == "coffee":
        total = 1.50 * quantity
        return print(f'{total:.2f}')
    elif product_i == "water":
        total = 1.00 * quantity
        return print(f'{total:.2f}')
    elif product_i == "coke":
        total = 1.40 * quantity
        return print(f'{total:.2f}')
    elif product_i == "snacks":
        total = 2.00 * quantity
        return print(f'{total:.2f}')


product_input = input()
quantity_input = int(input())
product_calculator(product_input, quantity_input)

