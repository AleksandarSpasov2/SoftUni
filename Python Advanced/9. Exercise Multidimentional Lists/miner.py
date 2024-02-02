n = int(input())
commands = input().split()

total_coal = 0
total_coal_collected = 0
miner = []
matrix = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
for row in range(n):
    matrix.append(input().split())

    if "s" in matrix[row]:
        miner = [row, matrix[row].index("s")]
        matrix[miner[0]][miner[1]] = '*'

    if 'c' in matrix[row]:
        total_coal += matrix[row].count('c')

for command in commands:
    r, c = miner[0] + directions[command][0], miner[1] + directions[command][1]

    if not (0 <= r < n and 0 <= c < n):
        break

    miner = [r, c]

    if matrix[r][c] == 'c':
        total_coal_collected += 1

        if total_coal_collected == total_coal:
            print(f"You collected all coal! ({r}, {c})")
            break

    elif matrix[r][c] == 'e':
        print(f"Game over! ({r}, {c})")
        break

    matrix[r][c] = '*'

else:
    print(f"{total_coal - total_coal_collected} pieces of coal left. ({r}, {c})")
