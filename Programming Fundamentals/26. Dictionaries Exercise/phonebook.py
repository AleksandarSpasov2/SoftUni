phone_book = {}

while True:
    entry = input()

    if "-" not in entry:
        break

    name, number = entry.split("-")

    phone_book[name] = number

entry_number = int(entry)

for person in range(entry_number):
    name_input = input()
    if name_input in phone_book.keys():
        print(f'{name_input} -> {phone_book[name_input]}')
    else:
        print(f'Contact {name_input} does not exist.')