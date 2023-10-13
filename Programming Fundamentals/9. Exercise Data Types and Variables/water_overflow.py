n = int(input())

capacity = 255
total_water = 0

for i in range(n):
    water = int(input())
    if total_water + water <= capacity:
        total_water += water
    else:
        print("Insufficient capacity!")

print(total_water)
