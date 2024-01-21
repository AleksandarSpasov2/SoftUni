text = input()

text_set = {}

for char in text:
    if char not in text_set:
        text_set[char] = 0
    text_set[char] += 1

for key, value in sorted(text_set.items()):
    print(f'{key}: {value} time/s')
