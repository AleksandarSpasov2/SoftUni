total_presents = int(input())
n = int(input())

matrix = []
s_pos = []
total_good_kids = 0
count_nice_kids = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(n):
    matrix.append(input().split())

    if 'S' in matrix[row]:
        s_pos = [row, matrix[row].index("S")]

    if 'V' in matrix[row]:
        total_good_kids += matrix[row].count('V')

count_nice_kids = total_good_kids

while True:
    command = input()

    if command == "Christmas morning":
        break

    r, c = s_pos
    matrix[r][c] = '-'
    r += directions[command][0]
    c += directions[command][1]

    if matrix[r][c] == 'X':
        matrix[r][c] = '-'

    if matrix[r][c] == "C":
        first_position = r, c
        for pos in directions.values():
            new_r, new_c = r + pos[0], c + pos[1]
            if 0 <= new_r < n and 0 <= new_c < len(matrix[0]):
                if matrix[new_r][new_c] == 'V':
                    total_presents -= 1
                    total_good_kids -= 1
                elif matrix[new_r][new_c] == 'X':
                    matrix[new_r][new_c] = '-'

    if matrix[r][c] == "V":
        total_presents -= 1
        total_good_kids -= 1
        matrix[r][c] = '-'

    matrix[r][c] = 'S'

    if total_presents <= 0 and total_good_kids > 0:
        print("Santa ran out of presents!")
        break

if total_presents <= 0 and total_good_kids <= 0:
    print(f'Good job, Santa! {count_nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {total_good_kids} nice kid/s.')

# Print the matrix
for row in matrix:
    print(' '.join(row))
