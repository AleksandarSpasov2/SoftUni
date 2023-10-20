def multiply_list(items):
    total = 1
    for i in items:
        total *= i
    return total
print(multiply_list([1, 2, -8]))