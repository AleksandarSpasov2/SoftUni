def main():
    elements = input().split()
    bakery = {}
    dict_add(elements, bakery)
    searched_products = input().split()
    for product in searched_products:
        if product in bakery:
            print(f"We have {bakery[product]} of {product} left")
        else:
            print(f"Sorry, we don't have {product}")


def dict_add(elements, bakery):
    for i in range(0, len(elements), 2):
        key = elements[i]
        value = elements[i + 1]
        bakery[key] = int(value)


main()