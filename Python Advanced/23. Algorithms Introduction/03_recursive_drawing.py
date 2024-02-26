def recursive_draw(n):
    if n == 0:
        return

    print('*' * n)

    recursive_draw(n - 1)

    print('#' * n)



n = int(input())
recursive_draw(n)