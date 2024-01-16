sequence = [int(x) for x in input().split()]
rack_space = int(input())

total_racks = 1
current_rack = rack_space

while sequence:

    cloth = sequence.pop()

    if current_rack >= cloth:
        current_rack -= cloth

    else:
        total_racks += 1
        current_rack = rack_space - cloth

print(total_racks)