def main():

    cupid_location = 0

    string_input = list(map(int, input().split("@")))

    while True:
        command = input()

        if command == "Love!":
            break

        command_input = command.split()

        if command_input[0] == "Jump":
            jump_length = int(command_input[1])
            cupid_location = (cupid_location + jump_length) % len(string_input)

            string_input[cupid_location] -= 2

            if string_input[cupid_location] == 0:
                print(f"Place {cupid_location} has Valentine's day.")
            elif string_input[cupid_location] < 0:
                print(f"Place {cupid_location} already had Valentine's day.")

    print(f"Cupid's last position was {cupid_location}.")

    failed_places = sum(1 for hearts in string_input if hearts > 0)

    if failed_places == 0:
        print("Mission was successful.")
    else:
        print(f"Cupid has failed {failed_places} places.")


main()
