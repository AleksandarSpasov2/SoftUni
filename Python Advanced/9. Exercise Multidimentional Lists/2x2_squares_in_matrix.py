row, col = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(row)]

same_block = 0

for r in range(row - 1):
    for c in range(col - 1):
        symbol = matrix[r][c]

        if symbol == matrix[r][c + 1] and symbol == matrix[r + 1][c] and symbol == matrix[r + 1][c + 1]:
            same_block += 1

print(same_block)