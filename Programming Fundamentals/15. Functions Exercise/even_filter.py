def is_odd(x):
    return x % 2 == 0

user_input = input()
user_input = user_input.split()

new_list = []
for element in user_input:
    new_list.append(int(element))

result = list(filter(is_odd, new_list))
print(result)