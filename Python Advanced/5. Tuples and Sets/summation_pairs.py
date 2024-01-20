sequence = [int(x) for x in input().split()]
target_number = int(input())


for element in range(len(sequence) + 1):
    if sequence[element] == '':
        continue
    for second_element in range(element + 1, len(sequence)):
        if sequence[second_element] == '':
            continue
        if sequence[element] + sequence[second_element] == target_number:
            print(f'{sequence[element]} + {sequence[second_element]} = {target_number}')
            sequence[element] = ''
            sequence[second_element] = ''
            break
