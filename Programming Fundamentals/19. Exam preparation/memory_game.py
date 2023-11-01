def main():
    sequence_of_element = input().split()
    count_of_moves = 0
    command = input()

    while command != "end":
        count_of_moves += 1
        index1, index2 = map(int, command.split())
        if is_valid(index1, index2, sequence_of_element):
            handle_invalid_input(sequence_of_element, count_of_moves)
        else:
            handle_valid_input(index1, index2, sequence_of_element, count_of_moves)

        if len(sequence_of_element) == 0:  # If all pairs are matched, exit
            print(f"You have won in {count_of_moves} turns!")
            return

        command = input()

    if len(sequence_of_element) > 0:  # If the game ended with the "end" command and there are still elements
        print(f'Sorry you lose :(\n{" ".join(sequence_of_element)}')


def is_valid(index1, index2, sequence):
    return (
            index1 == index2
            or index1 < 0
            or index2 < 0
            or index1 > len(sequence) - 1
            or index2 > len(sequence) - 1
    )


def handle_invalid_input(sequence, count_of_moves):
    middle_index = len(sequence) // 2
    sequence.insert(middle_index, f'-{count_of_moves}a')
    sequence.insert(middle_index, f'-{count_of_moves}a')
    print("Invalid input! Adding additional elements to the board")


def handle_valid_input(index1, index2, sequence, count_of_moves):
    if sequence[index1] == sequence[index2]:
        print(f"Congrats! You have found matching elements - {sequence[index1]}!")
        if index1 > index2:
            sequence.pop(index1)
            sequence.pop(index2)
        else:
            sequence.pop(index2)
            sequence.pop(index1)
    else:
        print("Try again!")


main()
