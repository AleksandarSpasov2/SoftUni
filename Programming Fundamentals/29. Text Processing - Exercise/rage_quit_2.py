message = input()
final_message = ''
repetition = ''
current_phrase = ''

for index in range(len(message)):
    if not message[index].isdigit():
        current_phrase += message[index].upper()
    else:
        for next_number in range(index, len(message)):
            if not message[next_number].isdigit():
                break
            repetition += message[next_number]
        final_message += int(repetition) * current_phrase
        current_phrase = ''
        repetition = ''

print(f"Unique symbols used: {len(set(final_message))}")
print(final_message)
