def sum_list(numbers_input):
    numbers_input_sum = []
    for num in numbers_input:
        number = 0
        for element in num:
            number += element
        numbers_input_sum.append(number)
        number = 0


numbers_input = list(map(int, input().split()))
string_input = input()
new_message = ''
