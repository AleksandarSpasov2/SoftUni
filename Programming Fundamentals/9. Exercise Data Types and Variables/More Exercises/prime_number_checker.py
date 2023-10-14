num = int(input())

if num <= 0:
    is_prime = False

else:
    is_prime = True

    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Yes")
else:
    print("NO")