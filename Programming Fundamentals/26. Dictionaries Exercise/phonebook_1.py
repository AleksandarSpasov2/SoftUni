phonebook_dict = {}
user_input = input()

while True:
    if "-" not in user_input:
        n = int(user_input)
        break
    name, phone_number = user_input.split("-", 1)  # Split only once to allow hyphens in phone numbers
    phonebook_dict[name] = phone_number
    user_input = input()

for _ in range(n):
    search_name = input()
    if search_name in phonebook_dict:
        print(f'{search_name} -> {phonebook_dict[search_name]}')
    else:
        print(f"Contact {search_name} does not exist.")
