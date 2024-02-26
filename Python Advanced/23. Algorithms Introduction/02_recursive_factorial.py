def recursive_fac(n):
    if n == 1:
        return 1

    return n * recursive_fac(n - 1)


n = int(input())
print(recursive_fac(n))