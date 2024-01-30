row, col = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(row)]

maximum_sum = 0
sub_matrix = []

for row_data in range(row - 2):
    first_line = matrix[row_data][:row_data + 2]
