list_int = input().split()
numbers_to_remove = int(input())

list_as_int = []

for number in list_int:
    list_as_int.append(int(number))

for removable in range(numbers_to_remove):
    smallest_number = 0
    for current_number in range(1, len(list_int)):
        if list_as_int[current_number] < list_as_int[smallest_number]:
            smallest_number = current_number
        list_as_int.pop(smallest_number)

print(list_as_int)

