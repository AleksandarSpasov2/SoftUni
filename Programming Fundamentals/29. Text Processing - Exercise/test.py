tickets = input().split(", ")

for ticket in tickets:
    if len(ticket) == 20:
        left_part = ticket[10:]
        right_part = ticket[:10]

        print(left_part)
        print(right_part)