import re


patter = r'(w{3}\.[A-Za-z0-9\-\.]+\.[a-z]+)'
line = input()
while line:
    match = re.search(patter, line)
    if match:
        valid = match.group(1)
        print(valid)
    line = input()

