import re

sentence = input()
word = input()

pattern = fr'(?i)\b{word}\b'

match = re.findall(pattern, sentence)

print(len(match))