rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

while True:
    command, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]