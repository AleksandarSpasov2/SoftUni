n = int(input())
matrix = []

bunny_loc = []
best_path = []
best_direction = None
total_eggs = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(n):
    matrix.append(input().split())
    if 'B' in matrix[row]:
        bunny_loc = [row, matrix[row].index('B')]

for direction, position in directions.items():
    r, c = [bunny_loc[0] + position[0], bunny_loc[1] + position[1]]
    eggs_collected = 0
    path = []
    while 0 <= r < n and 0 <= c < n:
        if matrix[r][c] == 'X':
            break
        eggs_collected += int(matrix[r][c])
        path.append([r, c])

        r += position[0]
        c += position[1]

        if eggs_collected > total_eggs:
            total_eggs = eggs_collected
            best_path = path
            best_direction = direction

print(best_direction)
print(*best_path, sep='\n')
print(total_eggs)