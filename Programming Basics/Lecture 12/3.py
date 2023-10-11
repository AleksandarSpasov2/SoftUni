
money_needed = float(input())
money_atm = float(input())

spend_count = 0
days = 0
total_money = 0

total_money = money_atm

while True:
    action = str(input())
    days += 1
    money_input = float(input())

    if total_money < 0:
        total_money = 0

    if action == "spend":
        spend_count += 1
        total_money -= money_input

        if spend_count == 5:
            print(f"You can't save the money.")
            print(f'{days}')
            break

    if action == "save":
        total_money += money_input
        if total_money >= money_needed:
            print(f'You saved the money for {days} days.')
            break
        continue




