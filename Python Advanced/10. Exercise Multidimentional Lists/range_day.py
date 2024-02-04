SIZE = 5

hunt_pos = []
matrix = []

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
    command = input()
    