list_input = input().split()
n = int(input())

list_input_int = []

for n_1 in list_input:
    list_input_int.append(int(n_1))

for removable in range(n):
    smallest_index = 0
    for current_index in range(1, len(list_input_int)):
        if list_input_int[current_index] < list_input_int[smallest_index]:
            smallest_index = current_index
    list_input_int.pop(smallest_index)

# Convert the remaining integers back to strings for printing
new_list = [str(num) for num in list_input_int]

# Join the numbers with ", " and print the result
result = ", ".join(new_list)
print(result)
