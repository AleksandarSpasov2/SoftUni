row, cow = [int(x) for x in input().split(', ')]

matrix = []
total_amount = 0

for i in range(cow):
    row_data = [int(x) for x in input().split(', ')]
    total_amount += sum(row_data)
    matrix.append(row_data)

print(total_amount)
print(matrix)