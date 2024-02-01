n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

coordinates = ((int(x) for x in c.split(', ')) for c in input().split())

directions = (
    (0, 1), # right
    (1, 0), # down
    (0, -1), # left
    (-1, 0), # up
    (1, 1), # bottom-right
    (-1, -1), # top_left
    (-1, 1), # top-right
    (1, -1), # bottom-left
    (0, 0) # current
)

for row, col in coordinates:
    if matrix[row][col] < 0:
        continue
    

