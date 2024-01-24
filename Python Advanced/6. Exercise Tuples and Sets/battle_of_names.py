event_set = set()
odd_set = set()

for row in range(1, int(input()) + 1):
    ascii_sum = sum(ord(l) for l in input()) // row

    if ascii_sum % 2 == 0:
        event_set.add(ascii_sum)
    else:
        odd_set.add(ascii_sum)

sum_odd_set, sum_even_set = sum(odd_set), sum(event_set)

if sum_even_set == sum_odd_set:
    print(*odd_set.union(event_set), sep=", ")
elif sum_even_set < sum_odd_set:
    print(*odd_set.difference(event_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(odd_set), sep=", ")

