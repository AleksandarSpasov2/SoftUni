words_input = input().split()
new_dict = {}

for word in words_input:
    word_lower = word.lower()
    if word_lower not in new_dict:
        new_dict[word_lower] = 0
    new_dict[word_lower] += 1

for key, value in new_dict.items():
    if value % 2 != 0:
        print(key, end=" ")

