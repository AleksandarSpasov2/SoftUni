def valid_coordinates(coordinates):
    return {coordinates[0], coordinates[2]}.issubset(valid_rows) and {coordinates[1], coordinates[3]}.issubset(valid_cols)


def swap_coordinates(coordinates, command):
    if command == 'swap' and len(coordinates) == 4 and valid_coordinates(coordinates):
        row1, col1, row2, col2 = coordinates
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print(f'Invalid input!')


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)

while True:
    command, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]

    if command == "END":
        break

    swap_coordinates(coordinates, command)