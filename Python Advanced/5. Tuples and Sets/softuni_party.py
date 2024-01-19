guests = set()

for guest in range(int(input())):
    guests.add(guest)

command = input()
while command != "END":
    if command in guests:
        guests.remove(command)
    command = input()

print(len(guests))
for n in sorted(guests):
    print(n)
