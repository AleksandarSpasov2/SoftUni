def closes_to_center(x1, y1, x2, y2):

    distance_1 = (x1 ** 2 + y1 ** 2) ** 0.5
    distance_2 = (x2 ** 2 + y2 ** 2) ** 0.5

    if distance_1 <= distance_2:
        return f'({x1}, {y1})'
    else:
        return f'({x2}, {y2})'


x_1 = int(input())
y_1 = int(input())
x_2 = int(input())
y_2 = int(input())
print(closes_to_center(x_1, y_1, x_2, y_2))