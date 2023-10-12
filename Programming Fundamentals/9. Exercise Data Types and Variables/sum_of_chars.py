
user_input = int(input())
total_sum = 0

for i in range(user_input):
    user_letter_input = str(input())
    total_sum += ord(user_letter_input)

print(f'The sum equals: {total_sum}')
