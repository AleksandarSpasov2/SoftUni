row, col = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(row):
    row_data = [int(x) for x in input().split()]
    matrix.append(row_data)

for col_data in range(col):
    col_sum = 0
    for row_data in range(row):
        col_sum += matrix[row_data][col_data]
    print(col_sum)