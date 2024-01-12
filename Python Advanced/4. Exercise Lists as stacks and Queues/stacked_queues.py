stack = []
n = int(input())

for _ in range(n):
    queries = input()
    data = queries.split()
    if data[0] == '1':
        number = int(data[1])
        stack.append(number)
    elif data[0] == '2':
        if stack:
            stack.pop()
    elif data[0] == '3':
        print(max(stack))
    elif data[0] == '4':
        print(min(stack))

while stack:

    print(stack.pop(), end=', ')