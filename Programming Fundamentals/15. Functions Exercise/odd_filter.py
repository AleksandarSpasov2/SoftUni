def is_odd(n):
    return n % 2 != 0


user_input = input().split()

user_input_int = []
for element in user_input:
    user_input_int.append(int(element))

odd_result = list(filter(is_odd, user_input_int))
print(odd_result)
