from math import ceil

budget = float(input())
number_of_student = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())

total_money_spent = 0
flour_counter = 0
eggs_counter = 0
apron_counter = 0

for i in range(number_of_student):
    flour_counter += 1
    eggs_counter += 10
    apron_counter += 1

flour_cost = (flour_counter - flour_counter // 5) * flour_price
egg_cost = eggs_counter * egg_price
total_aprons_needed = apron_counter + ceil(0.20 * apron_counter)
apron_cost = total_aprons_needed * apron_price
total_money_spent = flour_cost + egg_cost + apron_cost

if total_money_spent <= budget:
    print(f"Items purchased for {total_money_spent:.2f}$.")
else:
    print(f"{total_money_spent - budget:.2f}$ more needed.")
