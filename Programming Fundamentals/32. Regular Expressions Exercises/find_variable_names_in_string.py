import re

string = input()
patter = r'\b_([A-Za-z0-9]+)\b'

matches = re.findall(patter, string)

print(",".join(matches))
    