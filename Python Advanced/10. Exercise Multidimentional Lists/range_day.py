def move_command(command):
    direction, step = command[1], int(command[2])

    r = hunt_pos[0] + directions[direction][0] * step
    c = hunt_pos[1] + directions[direction][1] * step

    if matrix[r][c] == 'x':
        return hunt_pos

    if not (0 < +r < SIZE and 0 <= c < SIZE):
        return hunt_pos

    return [r, c]


def shoot_command(command):
    direction = command[1]
    r = hunt_pos[0] + directions[direction][0]
    c = hunt_pos[1] + directions[direction][1]

    while 0 <= r < SIZE and 0 <= c < SIZE:
        if matrix[r][c] == 'x':
            matrix[r][c] = '.'
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]



SIZE = 5

hunt_pos = []
matrix = []
targets_taken_down = 0
targets = 0
targets_hit_pos = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(SIZE):
    matrix.append(input().split())

    if "A" in matrix[row]:
        hunt_pos = [row, matrix[row].index("A")]

    targets += matrix[row].count('x')

for _ in range(int(input())):
    command = input().split()
    if command[0] == 'move':
        move_command(command)
    elif command[0] == 'shoot':
        shoot_command(command)
        if shoot_command:
            targets_taken_down += 1
            targets_hit_pos.append(shoot_command)
