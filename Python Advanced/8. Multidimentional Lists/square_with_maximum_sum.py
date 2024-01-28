row, col = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(row):
    row_data = [int(x) for x in input().split(', ')]
    matrix.append(row_data)


sub_matrix = []
maximum_sum = 0

for row_data in range(row - 1):
    for col_data in range(col - 1):
        current_element = matrix[row_data][col_data]
        right_element = matrix[row_data][col_data + 1]
        under_element = matrix[row_data + 1][col_data]
        diagonal_element = matrix[row_data + 1][col_data + 1]
        total_sum = current_element + right_element + under_element + diagonal_element
        if maximum_sum < total_sum:
            maximum_sum = total_sum
            sub_matrix = [[current_element, right_element], [under_element, diagonal_element]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(maximum_sum)