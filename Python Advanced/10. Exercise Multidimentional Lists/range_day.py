def move_command(command, hunt_pos):
    direction, step = command[1], int(command[2])
    r, c = hunt_pos[0], hunt_pos[1]
    r = directions[direction][0] * step
    c = directions[direction][1] * step




SIZE = 5

hunt_pos = []
matrix = []
targets_taken_down = 0

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

for _ in range(int(input())):
    command = input().split()
    if command[0] == 'move':
        pass
    elif command[0] == 'shoot':
        pass

