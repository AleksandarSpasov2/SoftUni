import re

n = int(input())
pattern = r'^(%|\$)([A-Z][a-z]{2,})\1: \[([0-9]+)\]\|\[([0-9]+)\]\|\[([0-9]+)\]\|$'

for _ in range(n):
    message = input()
    match = re.match(pattern, message)
    if match:
        tag = match.group(2)
        decrypted_message = ''.join(chr(int(match.group(i))) for i in range(3, 6))
        print(f"{tag}: {decrypted_message}")
    else:
        print("Valid message not found!")
