def main():
    product_dict = {}
    while True:
        product = input()

        if product == "buy":
            break

        product_item = product.split()
        item = product_item[0]
        price, quantity = float(product_item[1]), int(product_item[2])
        if item not in product_dict:
            product_dict[item] = {"price": price, "quantity": quantity}
        else:
            product_dict[item]["price"] += price
            product_dict[item]["quantity"] += quantity

    print_dict(product_dict, result=1)


def print_dict(product_dict, result=None):
    for key, value in product_dict.items():
        result = value["price"] * value["quantity"]
        print(f'{key} -> {result:.2f}')


main()


