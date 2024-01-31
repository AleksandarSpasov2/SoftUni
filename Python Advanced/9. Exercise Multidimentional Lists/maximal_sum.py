row, col = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(row)]

maximum_sum = float('-inf')
sub_matrix = []

for row_data in range(row - 2):
    for col_data in range(col - 2):
        first_line = matrix[row_data][col_data:col_data + 3]
        second_line = matrix[row_data + 1][col_data:col_data + 3]
        third_row = matrix[row_data + 2][col_data:col_data + 3]

        current_sum = sum(first_line) + sum(second_line) + sum(third_row)

        if maximum_sum <= current_sum:
            maximum_sum = current_sum
            sub_matrix = [first_line, second_line, third_row]

print(f"Sum = {maximum_sum}")
[print(*row) for row in sub_matrix]