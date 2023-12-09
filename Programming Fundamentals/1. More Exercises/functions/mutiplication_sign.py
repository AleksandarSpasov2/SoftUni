def multiplication_function(first, second, third):
    if first < 0 or second < 0 or third <0:
        return f'negative'
    elif first == 0 or second == 0 or third == 0:
        return f'zero'
    elif first > 0 and second > 0 and third > 0:
        return f'positive'


fist = int(input())
second = int(input())
third = int(input())

print(multiplication_function(fist, second, third))
