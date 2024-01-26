from collections import deque

words = deque(input().split())

all_colors = {'red', 'yellow', 'blue', 'orange', 'purple', 'green'}

req_colors = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'yellow', 'blue'},
}

result = []

while words:
    first_part = words.popleft()
    second_part = words.pop() if words else ""

    for color in (first_part + second_part, second_part + first_part):
        if color in all_colors:
            result.append(color)
            break
    else:
        for el in (first_part[:-1], second_part[:-1]):
            if el:
                words.insert(len(words) // 2, el)

for color in set(req_colors.keys()).intersection(result):


