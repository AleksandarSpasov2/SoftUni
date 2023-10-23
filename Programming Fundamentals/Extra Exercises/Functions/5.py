def test_range(int_input):
    if int_input in range(3,9):
        return print(f'Number is within ght range')
    else:
        return print(f'Number is not within the range')


user_input = int(input())
test_range(user_input)
