import re

pattern = r'%([A-Z][a-z]+)%<(.+)>\|([\d])\|(\d+.?\d)\$'
total_income = 0
user_input = input()

while user_input != 'end of shift':

    match = re.search(pattern, user_input)
    if match:
        result = match.groups()
        first_name = match.group(1)
        product = match.group(2)
        count = int(match.group(3))
        price = float(match.group(4))
        total = count * price
        total_income += total
        print(f'{first_name}: {product} - {total:.2f}')
    user_input = input()
print(f'Total income: {total_income:.2f}')