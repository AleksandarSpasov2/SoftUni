

user_input = str(input())

upper_cases = []

for index, char in enumerate(user_input):
    if char.isupper():
        upper_cases.append(index)


print(upper_cases)






