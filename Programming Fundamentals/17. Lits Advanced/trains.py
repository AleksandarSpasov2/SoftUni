wagoons = [0] * int(input())

while True:
    command = input().split()

    if command[0] == "End":
        print(wagoons)
        break

    elif command[0] == "add":
        people = int(command[1])
        wagoons[-1] += people

    elif command[0] == "insert":
        index = int(command[1])
        people = int(command[2])
        wagoons[index] += people

    elif command[0] == "leave":
        index = int(command[1])
        people = int(command[2])
        wagoons[index] -= people

