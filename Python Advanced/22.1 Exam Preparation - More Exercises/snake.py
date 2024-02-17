n = int(input())

matrix = []

position = []
burrow_position = []

food = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(n):
    line = list(input())
    matrix.append(line)

    if 'S' in line:
        position = [row, line.index("S")]
        matrix[position[0]][position[1]] = '-'

    if "B" in line:
        burrow_position.append([row, line.index("B")])

while food < 10:
    command = input()

    r = position[0] + directions[command][0]
    c = position[1] + directions[command][1]

    

    if matrix[r][c] == '*':
        food += 1

