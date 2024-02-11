from functools import reduce


def operate(operator, *args):
    if operator == '+':
        return reduce(lambda x, y: x + y, args)
    elif operator == '-':
        return reduce(lambda x, y: x - y, args)
    elif operator == '*':
        return reduce(lambda x, y: x * y, args)
    elif operator == '/':
        return reduce(lambda x, y: x / y if x != 0 or y != 0 else x, args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
