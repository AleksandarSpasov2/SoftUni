def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return f"Enter valid values!"

    else:
        area = length * width

        perimeter = (length * 2) + (width * 2)

        return f'Rectangle area: {area} Rectangle perimeter: {perimeter}'


print(rectangle('2', 10))
print(rectangle(2, 10))
