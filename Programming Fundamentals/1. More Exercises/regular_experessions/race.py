import re

participants = input().split(", ")

info = input()

while info != 'end of race':
    match_name = ''.join(re.findall(r'[a-z]', info, re.IGNORECASE))
    match_number = ''.join(re.findall(r'\d', info))
    print(match_name)
    print(match_number)
    info = input()
