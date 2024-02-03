string_input = [x.split() for x in input().split("|")]
print(*[' '.join(x) for x in string_input[::-1]])