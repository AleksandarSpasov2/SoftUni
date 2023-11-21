def reverse_text(text: str):
    reversed_text = text[::-1]
    return reversed_text


def print_half_text(text: str):
    length = len(text) / 2
    half_text = text[length::]
    return half_text


text_name = 'abcd'

new_text = text_name[::-1]

print(new_text)

print(reverse_text(text_name))

print(print_half_text(text_name))
