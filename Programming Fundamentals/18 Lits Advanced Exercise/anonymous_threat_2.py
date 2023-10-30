# Read the initial data
data = input().split()
commands = []

while True:
    command = input()
    if command == "3:1":
        break
    commands.append(command)

for command in commands:
    parts = command.split()
    operation = parts[0]

    if operation == "merge":
        start_index, end_index = map(int, parts[1:])
        if start_index < 0:
            start_index = 0
        if end_index >= len(data):
            end_index = len(data) - 1
        data[start_index:end_index + 1] = [''.join(data[start_index:end_index + 1])]
    elif operation == "divide":
        index, partitions = map(int, parts[1:])
        element = data[index]
        partition_size = len(element) // partitions
        extra_chars = len(element) % partitions

        divided_parts = []
        start = 0

        for i in range(partitions):
            end = start + partition_size + (1 if i < extra_chars else 0)
            divided_parts.append(element[start:end])
            start = end

        data[index:index + 1] = divided_parts

result = ' '.join(data)
print(result)
