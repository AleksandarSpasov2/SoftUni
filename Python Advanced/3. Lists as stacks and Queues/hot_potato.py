from collections import deque

names = deque(input().split())
n_toss = int(input()) - 1

while len(names) > 1:
    names.rotate(-n_toss)
    removed_name = names.popleft()
    print(f'Removed {removed_name}')

print(f'Last is {names.popleft()}')


