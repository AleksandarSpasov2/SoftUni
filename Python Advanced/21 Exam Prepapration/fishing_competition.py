n = int(input())

matrix = []

position = []
catch = 0

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

command = input()

while command != "collect the nets":

    r, c = directions[command]
    new_r = (position[0] + r) % n
    new_c = (position[1] + c) % n

    if matrix[new_r][new_c].isdigit():
        catch += int(matrix[new_r][new_c])
        matrix[new_r][new_c] = '-'

    position = [new_r, new_c]

    if matrix[position[0]][position[1]] == 'W':
        print(f'"You fell into a whirlpool!'
              f' The ship sank and you lost the fish you caught.'
              f' Last coordinates of the ship: [{position[0]},{position[1]}]"')
        exit()

    command = input()

matrix[position[0]][position[1]] = "S"

if catch >= 20:
    print(f"Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! "
          f"You need {20 - catch} tons of fish more.")

if catch > 0:
    print(f"Amount of fish caught: {catch} tons.")

print('\n'.join([''.join(row) for row in matrix]))
