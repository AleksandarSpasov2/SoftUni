def main():
    elements = input().split()
    bakery = {}
    dict_add(elements, bakery)
    


def dict_add(elements, bakery):
    for i in range(0, len(elements), 2):
        key = elements[i]
        value = elements[i + 1]
        bakery[key] = int(value)
