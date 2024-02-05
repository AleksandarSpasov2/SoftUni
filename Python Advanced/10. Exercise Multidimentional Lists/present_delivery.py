def eat_cookie(presents_left, nice_kids):
    for coordinates in directions.values():
        r = santa_pos[0] + coordinates[0]
        c = santa_pos[1] + coordinates[1]

        if matrix[r][c].isalpha():
            if matrix[r][c] == "V":
                nice_kids += 1

            matrix[r][c] = '-'
            presents_left -= 1

        if not presents_left:
            break

    return presents_left, nice_kids


total_presents = int(input())
n = int(input())

matrix = []
santa_pos = []
total_good_kids = 0
nice_kids_visited = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(n):
    matrix.append(input().split())

    if 'S' in matrix[row]:
        santa_pos = [row, matrix[row].index("S")]

    if 'V' in matrix[row]:
        total_good_kids += matrix[row].count('V')


command = input()

while command != "Christmas morning":
    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1],
    ]

    house = matrix[santa_pos[0]][santa_pos[1]]

    if house == "V":
        nice_kids_visited += 1
        total_presents -= 1
    elif house == 'C':
        total_presents, nice_kids_visited = eat_cookie(total_presents,nice_kids_visited)

    matrix[santa_pos[0]][santa_pos[1]] = '-'

    if not total_presents or nice_kids_visited == total_good_kids:
        break
    command = input()

matrix[santa_pos[0]][santa_pos[1]] = "S"

if not total_presents and nice_kids_visited < total_good_kids:
    print("Santa ran out of presents!")

[print(*row) for row in matrix]

if nice_kids_visited == total_good_kids:
    print(f'Good job, Santa! {total_good_kids} happy nice kid/s.')
else:
    print(f'No presents for {total_good_kids - nice_kids_visited} nice kid/s.')

