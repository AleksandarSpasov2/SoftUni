n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

command = input().split()

while command[0] != "END":

    sub_command, row, col, value = [int(x) if x.isdigit() else x for x in command]

    if not (0 <= row < n and 0 <= col < n):
        print(f"Invalid coordinates")

    if sub_command == "Add":
        matrix[row][col] += value
    elif sub_command == "Subtract":
        matrix[row][col] -= value

    command = input().split()

[print(*row) for row in matrix]