number_list = list(map(int, input().split(", ")))
f_indices = [x for x in range(len(number_list)) if x % 2 == 0]
print(f_indices)