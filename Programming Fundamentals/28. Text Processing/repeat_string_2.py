string_input = input().split()

new_string = ''

for word in string_input:
    new_string += len(word) * word

print(new_string)