from collections import deque

people = deque()

quantity = int(input())

name = input()
while name != "Start":
    people.append(name)
    name = input()

command = input()
while command != "End":
    data = command.split()
    if len(data) == 1:
        liters = data[0]
        liters = int(liters)
        person = people.popleft()
        if liters <= quantity:
            quantity -= liters
            print(f"{person} got water")
        else:
            print(f"{person} must wait")

    else:
        liters = int(data[1])
        quantity += liters

    command = input()

print(f"{quantity} liters left")
