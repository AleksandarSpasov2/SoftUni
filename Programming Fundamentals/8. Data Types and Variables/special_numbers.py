number = int(input())

for current_number in range(1, number + 1):
    current_number_as_str = str(current_number)  # preobrazuvame v str za da mojem da vadim indexi
    digit_sum = 0
    is_special = False

    for digit in current_number_as_str:
        digit_sum += int(digit)             # preobrazuvame obratno v int

    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        is_special = True

    print(f'{current_number} -> {is_special} ')


