num = int(input())

if num <= 0:
    is_prime = False
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False

print(is_prime)