sequence_int = [int(s) for s in input().split()]

removed_elements_sum = 0

while sequence_int:
    received_int = int(input())
    if received_int < 0:
        removed_index = sequence_int[0]
        sequence_int[0] = sequence_int[-1]

    elif received_int >= len(sequence_int):
        removed_index = sequence_int[-1]
        sequence_int[-1] = sequence_int[0]

    else:
        removed_index = sequence_int[received_int]
        sequence_int.pop(received_int)

    removed_elements_sum += removed_index

    for i in range(len(sequence_int)):
        if sequence_int[i] <= removed_index:
            sequence_int[i] += removed_index
        elif sequence_int[i] > removed_index:
            sequence_int[i] -= removed_index

print(removed_elements_sum)
