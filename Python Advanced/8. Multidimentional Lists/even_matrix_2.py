row = int(input())

matrix = []

for _ in range(row):
    row_data = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
    matrix.append(row_data)

print(matrix)