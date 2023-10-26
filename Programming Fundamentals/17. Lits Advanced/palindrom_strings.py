first_input = input().split()
second_input = input()

list_1 = []
for word in first_input:
    if word[::] == word[::-1]:
        list_1.append(word)

counter = 0
for word in list_1:
    if word.count(second_input):
        counter += 1

print(list_1)
print(f'Found palindrome {counter} times')
