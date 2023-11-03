def main():
    health = 100
    bitcoins = 0
    counter = 0
    dungeon_rooms = input().split("|")
    
    for room in dungeon_rooms:
        counter += 1
        room_split = room.split()
        command, number = room_split[0], int(room_split[1])

        if command == "potion":
            health += number

            if health > 100:
                current_heal = abs(health - number)
                health = 100
                print(f"You healed for {current_heal} hp.")
                print(f"Current health: {health} hp.")
            else:
                print(f"You healed for {number} hp.")
                print(f"Current health: {health} hp.")

        elif command == "chest":
            bitcoins += number
            print(f"You found {number} bitcoins.")

        else:
            health -= number
            if health > 1:
                print(f"You slayed {command}.")
            else:
                print(f"You died! Killed by {command}.")
                print(f"Best room: {counter}")
                exit()
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")


main()

