def print_numbers(numbers):
    positive_numbers = sum(num for num in numbers if num > 0)
    negative_numbers = sum(num for num in numbers if num < 0)

    print(positive_numbers)
    print(negative_numbers)
    if positive_numbers > abs(negative_numbers):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = [int(x) for x in input().split()]

print_numbers(numbers)
