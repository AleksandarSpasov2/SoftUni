def main():
    products = {}

    command = input()
    while command != "buy":
        name, price, quantity = command.split()
        quantity = int(quantity)
        price = float(price)

        if name not in products.keys():
            products[name] = []
        else:
            for value in 