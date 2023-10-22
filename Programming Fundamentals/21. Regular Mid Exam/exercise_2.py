route = input().split("||")
fuel_amount = int(input())
ammunition_amount = int(input())

for command in route:
    parts = command.split()
    action = parts[0]

    if action == "Travel":
        value = int(parts[1])
        if fuel_amount >= value:
            fuel_amount -= value
            print(f"The spaceship travelled {value} light-years.")
        else:
            print("Mission failed.")
            break

    elif action == "Enemy":
        value = int(parts[1])
        if ammunition_amount >= value:
            ammunition_amount -= value
            print(f"An enemy with {value} armour is defeated.")
        elif fuel_amount >= value * 2:
            fuel_amount -= value * 2
            print(f"An enemy with {value} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            break

    elif action == "Repair":
        value = int(parts[1])
        ammunition_amount += value * 2
        fuel_amount += value
        print(f"Ammunitions added: {value * 2}.")
        print(f"Fuel added: {value}.")

    elif action == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
