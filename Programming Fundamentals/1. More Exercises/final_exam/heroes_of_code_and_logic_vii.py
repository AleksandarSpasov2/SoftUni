def main():
    hero_dict = {}

    heroes_number = int(input())

    for hero in range(heroes_number):
        hero_name, hit_points, mana_points = input().split()
        mana_points = int(mana_points)
        hit_points = int(hit_points)

        if hero_name not in hero_dict:
            hero_dict[hero_name] = {'hp': 0, 'mp': 0}
        hero_dict[hero_name]['hp'] += hit_points
        hero_dict[hero_name]['mp'] += mana_points

        if hero_dict[hero_name]['hp'] > 100:
            hero_dict[hero_name]['hp'] = 100

        if hero_dict[hero_name]['mp'] > 200:
            hero_dict[hero_name]['mp'] = 200

    command = input().split(" - ")

    while command[0] != 'End':

        if command[0] == 'CastSpell':
            cast_spell_function(hero_dict, command)

        elif command[0] == 'TakeDamage':
            take_damage_function(hero_dict, command)

        elif command[0] == 'Recharge':
            recharge_function(hero_dict, command)

        elif command[0] == 'Heal':
            heal_function(hero_dict, command)

        command = input().split(" - ")

    print_function(hero_dict)


def cast_spell_function(hero_dict, command):

    hero_name, mp_needed, spell_name = command[1], command[2], command[3]
    mp_needed = int(mp_needed)

    if mp_needed <= hero_dict[hero_name]['mp']:
        hero_dict[hero_name]['mp'] -= mp_needed
        print(f'{hero_name} has successfully cast {spell_name} and now has {hero_dict[hero_name]["mp"]} MP!')

    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")


def take_damage_function(hero_dict, command):

    hero_name, damage, attacker = command[1], command[2], command[3]
    damage = int(damage)
    hero_dict[hero_name]['hp'] -= damage

    if hero_dict[hero_name]['hp'] <= 0:
        del hero_dict[hero_name]
        print(f"{hero_name} has been killed by {attacker}!")

    else:
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hero_dict[hero_name]['hp']} HP left!")


def recharge_function(hero_dict, command):

    hero_name, amount = command[1], command[2]
    amount = int(amount)

    start_amount = hero_dict[hero_name]['mp']
    hero_dict[hero_name]['mp'] += amount

    if hero_dict[hero_name]['mp'] > 200:
        hero_dict[hero_name]['mp'] = 200
        difference = 200 - start_amount
        print(f"{hero_name} recharged for {difference} MP!")

    else:
        print(f"{hero_name} recharged for {amount} MP!")


def heal_function(hero_dict, command):

    hero_name, amount = command[1], command[2]
    amount = int(amount)
    
    start_amount = hero_dict[hero_name]['hp']
    hero_dict[hero_name]['hp'] += amount

    if hero_dict[hero_name]['hp'] > 100:
        hero_dict[hero_name]['hp'] = 100
        difference = 100 - start_amount
        print(f"{hero_name} healed for {difference} HP!")

    else:
        print(f"{hero_name} healed for {amount} HP!")


def print_function(hero_dict):

    for key, value in hero_dict.items():

        print(key)
        print(f'  HP: {value["hp"]}')
        print(f'  MP: {value["mp"]}')


main()
