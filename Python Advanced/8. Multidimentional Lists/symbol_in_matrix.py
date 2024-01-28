n = int(input())

matrix = []

for _ in range(n):
    row_data = [x for x in input()]
    matrix.append(row_data)

searched_symbol = input()

for row in range(n):
    for col in range(n):
        if matrix[row][col] == searched_symbol:
            print(f'({row}, {col})')
            exit()
