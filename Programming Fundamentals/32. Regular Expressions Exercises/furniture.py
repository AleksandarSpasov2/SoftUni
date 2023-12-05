import re

pattern = '>>([A-Za-z]+)<<([0-9]+\.?\d*)!(\d+)'

total_cost = 0
furniture_list = []
command_input = input()
while command_input != "Purchase":
    match = re.search(pattern, command_input)
    if match:
        furniture, price, quantity = match.groups()
        furniture_list.append(furniture)
        total_cost += float(price) * int(quantity)
    command_input = input()

print(f'Bought furniture:')
for element in furniture_list:
    print(element)
print(f'Total money spend: {total_cost:.2f}')
