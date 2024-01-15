sequence = [int(x) for x in input().split()]
capacity = int(input())

total_racks = 1
available_capacity = 0


while True:
    if sequence:
        current_cloth = sequence.pop()
        available_capacity += current_cloth

        if available_capacity == capacity:
            total_racks += 1
            available_capacity = 0
        elif available_capacity > capacity:
            available_capacity = 0
            available_capacity += current_cloth
            total_racks += 1
    else:
        break

print(total_racks)