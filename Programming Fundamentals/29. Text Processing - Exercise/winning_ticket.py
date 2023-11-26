def main():
    tickets = input().split(", ")


def ticket_is_valid_characters(tickets):
    for ticket in tickets:
        if len(ticket) == 20:
            return True
        return False


def ticket_is_valid_symbols(tickets):
    for ticket in tickets:
        left_part = ticket[:10]
        right_part = ticket[11:]
