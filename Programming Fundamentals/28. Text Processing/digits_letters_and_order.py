string_input = input()

numbers = ""
characters = ''
other_characters = ''

for char in string_input:
    if char.isdigit():
        numbers += char
    elif char.isalpha():
        characters += char
    else:
        other_characters += char

print(numbers)
print(characters)
print(other_characters)
