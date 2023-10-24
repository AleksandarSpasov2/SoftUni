def all_char_in_between(first_input, second_input):
    final_list = []
    for character in range(ord(first_input) + 1, ord(second_input)):
        final_list.append(chr(character))
    return final_list


first = str(input())
second = str(input())
result = all_char_in_between(first, second)
print(" ".join(result))