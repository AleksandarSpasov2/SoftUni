n = int(input())
matrix = [list(input()) for _ in range(n)]

removed_knights = 0

moves = {
    (1, 2),
    (-1, -2),
    (2, 1),
    (-2, -1),
    (-1, 2),
    (1, -2),
    (2, -1),
    (-2, 1),
}

while True:
    max_attacks = 0
    knights_with_most_attacks_pos = []

    for row in range(n):
        for col in range(n):
            if matrix[row][col] == 'K':
                attacks = 0

                for pos in moves:
                    pos_r = row + pos[0]
                    pos_c = col + pos[1]

                    if 0 <= pos_r < n and 0 <= pos_c < n:
                        if matrix[pos_r][pos_c] == 'K':
                            attacks += 1

                if attacks > max_attacks:
                    max_attacks = attacks
                    knights_with_most_attacks_pos = [row, col]

    if knights_with_most_attacks_pos:
        r, c = knights_with_most_attacks_pos
        matrix[r][c] = '0'
        removed_knights += 1
    else:
        break

print(removed_knights)