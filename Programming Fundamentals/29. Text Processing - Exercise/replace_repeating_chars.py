text_input = input()
new_text = ''
last_char = ''
for character in text_input:
    if character != last_char:
        new_text += character
        last_char = character
print(new_text)