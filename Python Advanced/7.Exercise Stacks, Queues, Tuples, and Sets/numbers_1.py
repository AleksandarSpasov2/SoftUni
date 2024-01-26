first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

for _ in range(int(input())):
    command = input().split()
    if command[0] == "Add" and command[1] == "First":
        numbers = range(int(command[2]), int(command[-1])+1)
        first_sequence.add(int(x) for x in numbers)
    elif command[0] == "Remove" and command[1] == "First":
        numbers = range(int(command[2]), int(command[-1])+1)
        first_sequence.add(int(x) for x in numbers)
    elif command[0] == "Remove" and command[1] == "Second":
        numbers = range(int(command[2]), int(command[-1])+1)
        second_sequence.difference_update(int(x) for x in numbers)
    elif command[0] == 'Check':
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")

print(sorted(', '.join(str(x) for x in first_sequence)))
print(sorted(', '.join(str(x) for x in second_sequence)))

