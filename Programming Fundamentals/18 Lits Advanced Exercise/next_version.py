list_input = [int(digit) for digit in input().split(".")]

list_input[-1] += 1

for element in range(len(list_input)-1, -1, -1):
    if list_input[element] > 9:
        list_input[element] = 0
        list_input[element - 1] += 1


print(".".join(str(x) for x in list_input))

