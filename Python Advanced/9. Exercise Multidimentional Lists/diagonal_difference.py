num = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(num)]

primary, secondary = 0, 0

for i in range(num):
    primary += matrix[i][i]
    secondary += matrix[i][num - i - 1]

print(abs(primary - secondary))