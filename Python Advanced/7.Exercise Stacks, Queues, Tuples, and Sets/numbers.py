first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

for _ in range(int(input())):
    command = input().split()
    if command[0] == "Add" and command[1] == "First":
        numbers = range(int(command[2]), int(command[-1] + 1))
        first_sequence.add(int(x) for x in numbers)


