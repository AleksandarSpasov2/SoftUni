text = input().split()
command = input().split()

while command[0] != "3:1":
    if command[0] == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if end_index > len(text) - 1:
            end_index = len(text) - 1
        merged_element = "".join(text[start_index:end_index + 1])
        text[start_index:end_index + 1] = [merged_element]

    elif command[0] == "divide":
        index = int(command[1])
        partitions = int(command[2])
        element = text[index]
        divided_partition = []
        partition_lenght = len(element) // partitions
        for current_elelemnt_index in range(partitions):
            if current_elelemnt_index != partitions - 1:
                divided_partition.append(element[current_elelemnt_index * partition_lenght: (current_elelemnt_index + 1) * partition_lenght])
            else:
                divided_partition.append(element[current_elelemnt_index * partition_lenght:])


    command = input().split()

print(" ".join(text))
