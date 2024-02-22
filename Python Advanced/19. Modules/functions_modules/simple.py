def sum_of_numbers(*args):
    result = 0
    for num in args:
        result += num

    return result


def print_letter(*args):
    return [letter for letter in args]
