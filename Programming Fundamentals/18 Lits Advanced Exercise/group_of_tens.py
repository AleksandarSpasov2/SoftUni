sequence_of_numbers = [int(x) for x in input().split(", ")]

current_group = 10

while sequence_of_numbers:
    filtered_numbers = [number for number in sequence_of_numbers if number <= current_group]
    print(f"Group of {current_group}'s: {filtered_numbers}")
    current_group += 10
    sequence_of_numbers = [number for number in sequence_of_numbers if number not in filtered_numbers]



