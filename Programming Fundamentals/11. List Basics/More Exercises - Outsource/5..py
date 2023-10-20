my_list = input().split()

for words in my_list:
    str_count = 0
    if len(words) > 1 and words[0] == words[-1]:
        str_count += 1
print(str_count)



