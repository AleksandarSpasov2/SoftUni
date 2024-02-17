n = int(input())

matrix = []
position = []
armor = 300
enemy_planes = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}

for row in range(n):
    line = list(input())
    matrix.append(line)

    if 'J' in line:
        position = [row, line.index('J')]
        matrix[position[0]][position[1]] = '-'

    enemy_planes += line.count('E')

while enemy_planes != 0 and armor > 0:
    command = input()
    r, c = position[0] + directions[command][0], position[1] + directions[command][1]

    if matrix[r][c] == 'E':
        enemy_planes -= 1
        armor -= 100
        matrix[r][c] = '-'

    elif matrix[r][c] == 'R':
        armor = 300

    matrix[position[0]][position[1]] = '-'
    position = [r, c]
    matrix[r][c] = 'J'

    if enemy_planes == 0:
        print("Mission accomplished, you neutralized the aerial threat!")
        break
    elif armor <= 0:
        print(f"Mission failed, your jetfighter was shot down! Last coordinates [{r}, {c}]!")
        break

[print(''.join(row)) for row in matrix]
