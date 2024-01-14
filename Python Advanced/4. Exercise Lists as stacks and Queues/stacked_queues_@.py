

stack = []

for _ in range(int(input())):
    data_type = [int(x) for x in input().split()]
    command = data_type[0]

    if command == 1:
        stack.append(data_type[1])
    elif command == 2:
        if stack:
            stack.pop()
    elif command == 3:
        if stack:
            print(max(stack))
    elif command == 4:
        if stack:
            print(min(stack))

stack.reverse()
print(*stack, sep=', ')
