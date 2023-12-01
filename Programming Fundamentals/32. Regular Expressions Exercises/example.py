import re

while True:
    string = input()
    if not string:
        break

matches = re.findall(r'\d+', string)

for match in matches:
    print(match)


