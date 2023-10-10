

user_input = str(input())

lower_case = user_input.lower()

word_list = ["fish", "sun", "sand", "water"]

counter = 0

for word in word_list:
    counter += lower_case.count(word)

print(counter)

