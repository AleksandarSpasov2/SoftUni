lost_games_count = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

counter = 0
total_repairs = 0

for games in range(1, lost_games_count + 1):

    if games % 2 == 0:
        total_repairs += helmet_price

    if games % 3 == 0:
        total_repairs += sword_price

    if games % 3 == 0 and games % 2 == 0:
        counter += 1
        total_repairs += shield_price

    if counter == 2:
        counter = 0
        total_repairs += armor_price

print(f'Gladiator expenses: {total_repairs:.2f} aureus')
