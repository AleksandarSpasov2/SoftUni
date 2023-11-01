def multiplication_sign(input_1, input_2, input_3):
    if input_1 < 0 or input_2 < 0 or input_3 < 0:
        return f'negative'
    elif input_1 == 0 or input_2 == 0 or input_3 == 0:
        return  f'zero'
    elif input_1 > 0 and input_2 > 0 and input_3 > 0:
        return f'positive'


user_1 = int(input())
user_2 = int(input())
user_3 = int(input())
print(multiplication_sign(user_1, user_2, user_3))
