banned_words = input().split()
text_input = input()

result = ""
for word in banned_words:
    while word in text_input:
        lenght = len(word)
        result += text_input.replace(word, (lenght * "*"))

print(result)
