def is_even(number):
    if number % 2 == 0:
        return True
    return False


user_input = input().split()

user_input_as_int = []

for element in user_input:
    user_input_as_int.append(int(element))

even_list = []

for element in user_input_as_int:
    if is_even(element):
        even_list.append(element)

print(even_list)

