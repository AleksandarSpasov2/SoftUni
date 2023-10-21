def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_checker(list_new):
    are_primes = []
    for element in list_new:
        if is_prime(element):
            are_primes.append(True)
        else:
            are_primes.append(False)
    return are_primes


lis_1 = [0, 3, 4, 7, 9]
lis_2 = [3, 5, 7, 13]
lis_3 = [1, 5, 3]

result_1 = prime_checker(lis_1)
result_2 = prime_checker(lis_2)
result_3 = prime_checker(lis_3)

print(result_1)
print(result_2)
print(result_3)
