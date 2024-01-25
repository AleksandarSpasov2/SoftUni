first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

for _ in range(int(input())):
    command = input().split()
    if command[0] == "Add" and command[1] == "First":
        numbers = range(int(command[2]), int(command[-1]))
        first_sequence.add(int(x) for x in numbers)
    elif command[0] == "Remove" and command[1] == "First":
        numbers = range(int(command[2]), int(command[-1]))
        first_sequence.remove(int(x) for x in numbers)
    elif command[0] == "Remove" and command[1] == "Second":
        numbers = range(int(command[2]), int(command[-1]))
        second_sequence.remove(int(x) for x in numbers)
    elif command[0] == 'Check':
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")

print(sorted(*first_sequence), sep=', ')
print(sorted(*second_sequence), sep=', ')







