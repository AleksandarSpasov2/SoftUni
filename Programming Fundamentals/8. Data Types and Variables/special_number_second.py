n = int(input())

for number in range(1, n + 1):
    is_special = False
    n_as_str = str(number)
    digit_sum = 0

    for index in n_as_str:
        digit_sum += int(index)

    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        is_special = True

    print(f'{number} -> {is_special}')
