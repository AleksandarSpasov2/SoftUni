def length_is_valid(text):
    if 3 <= len(text) <= 16:
        return True
    return False


def letters_numbers_is_valid(text):
    for char in text:
        if not (char.isalnum() \
                or char == "-" \
                or char == "_"):
            return False
    return True


def redundant_is_valid(text):
    if " " in text:
        return False
    return True


def username_is_valid(text):
    if length_is_valid(text) \
            and letters_numbers_is_valid(text) \
            and redundant_is_valid(text):
        return True
    return False


username = input().split(", ")
for name in username:
    if username_is_valid(name):
        print(name)
