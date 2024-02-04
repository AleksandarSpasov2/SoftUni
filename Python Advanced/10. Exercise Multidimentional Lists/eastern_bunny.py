n = int(input())
matrix = []
bunny_location = []
best_path = []
max_eggs = 0
best_direction = None

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(n):
    matrix.append(input().split())
    if 'B' in matrix[row]:
        bunny_location = [row, matrix[row].index('B')]

for way, pos in directions.items():
    row, col = [bunny_location[0] + pos[0], bunny_location[1] + pos[1]]
    path = []
    collected_eggs = 0

    while 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == 'X':
            break

        collected_eggs += int(matrix[row][col])
        path.append([row, col])

        row += pos[0]
        col += pos[1]

        if collected_eggs > max_eggs:
            max_eggs = collected_eggs
            best_path = path
            best_direction = way

print(best_direction)
print(*best_path, sep='\n')
print(max_eggs)