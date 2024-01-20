n = int(input())

party_guests = set()

for _ in range(n):
    guest = input()
    party_guests.add(guest)

code = input()
while code != 'END':
    if code in party_guests:
        party_guests.remove(code)
    code = input()

print(len(party_guests))
for x in sorted(party_guests):
    print(x)