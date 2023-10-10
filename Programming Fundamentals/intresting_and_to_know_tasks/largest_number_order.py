



user_input = int(input())

largets_number = 0

while user_input > 0:
    digit = user_input % 10
    largets_number = largets_number * 10 + digit
    user_input //= 10

print(largets_number)





