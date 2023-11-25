def generate_rage_message(input_str):
    unique_symbols = set()
    rage_message = ""
    i = 0

    while i < len(input_str):
        symbol = input_str[i].upper()
        unique_symbols.add(symbol)
        i += 1

        count = 0
        while i < len(input_str) and input_str[i].isdigit():
            count = count * 10 + int(input_str[i])
            i += 1

        rage_message += symbol * count

    print(f"Unique symbols used: {len(unique_symbols)}")
    print(rage_message)


input_str = input()

generate_rage_message(input_str)
