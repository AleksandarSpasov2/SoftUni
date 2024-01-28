n = int(input())

matrix = []
total_sum = 0

for _ in range(n):
    row_data = [int(x) for x in input().split()]
    matrix.append(row_data)

for row in range(n):
    total_sum += matrix[row][row]

print(total_sum)