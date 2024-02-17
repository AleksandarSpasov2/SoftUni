from collections import deque

bomb_effect = deque([int(x) for x in input().split(", ")])
bomb_casings = [int(x) for x in input().split(", ")]

bombs = {
    'Datura Bombs': 40,
    'Cherry Bombs': 60,
    'Smoke Decoy Bombs': 120,
}
bombs_made_list = []

bombs_made = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0,

}

while bomb_casings and bomb_casings:
    current_effect = bomb_effect[0]

    current_casing = bomb_casings[-1]

    if current_effect + current_casing == 40 or current_casing + current_effect == 60 or current_casing + current_effect == 120:
        bombs_made_list.append(current_effect + current_casing)
        bomb_casings.pop()
        bomb_effect.popleft()
    else:
        bomb_casings[-1] -= 5

for element in bombs_made_list:
    for name, value in bombs.items():
        if element == value:
            bombs_made[name] += 1

if 0 in bombs_made.values():
    print("You don't have enough materials to fill the bomb pouch.")
else:
    print("Bene! You have successfully filled the bomb pouch!")

if not bomb_effect:
    print("Bomb Effects: empty")
else:
    print(f'Bomb Effects: {" ,".join(str(x) for x in bomb_effect)}')

if not bomb_casings:
    print("Bomb Casings: empty")
else:
    print(f'Bomb Casings: {" ,".join(str(x) for x in bomb_casings)}')

bombs_made = sorted(bombs_made.items())


for bomb in bombs_made:
    print(f'{bomb[0]}: {bomb[1]}')