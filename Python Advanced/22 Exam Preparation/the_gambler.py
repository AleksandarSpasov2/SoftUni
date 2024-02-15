n = int(input())

position = []
matrix = []

money = 100

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}

for row in range(n):
    line = list(input())
    matrix.append(line)
    if 'G' in line:
        position = [row, line.index("G")]
        matrix[position[0]][position[1]] = '-'


command = input()

while command != "end":
    r = position[0] + directions[command][0]
    c = position[1] + directions[command][1]
    position[0], position[1] = r, c

    if not 0 <= r < n or not 0 <= c < n:
        money = 0
        print("Game over! You lost everything!")
        exit()

    if matrix[r][c] == 'W':
        money += 100

    elif matrix[r][c] == 'P':
        money -= 200
        if money <= 0:
            break

    elif matrix[r][c] == 'J':
        money += 100000
        matrix[position[0]][position[1]] = 'G'
        print(f'You win the Jackpot!\n'
              f' End of the game. Total amount: {money}$"')
        [print(*row) for row in matrix]
        exit()

    matrix[r][c] = '-'

    command = input()

matrix[position[0]][position[1]] = 'G'
print(f"End of the game. Total amount: {money}$")
[print(*row) for row in matrix]
