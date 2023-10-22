user_input = input().split()

user_input_int = []

for element in user_input:
    user_input_int.append(int(element))

maximum_number = max(user_input_int)
minimum_number = min(user_input_int)
sum_of_list = sum(user_input_int)

print(f'The minimum number is {minimum_number}')
print(f'The maximum number is {maximum_number}')
print(f'The sum number is: {sum_of_list}')