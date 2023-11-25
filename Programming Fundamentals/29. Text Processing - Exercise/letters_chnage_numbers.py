def main():
    string_input = input().split()
    first_function(string_input)


def first_function(string_input):
    final_total_sum = 0
    for phrase in string_input:
        total_sum = 0
        phrase = phrase.strip()
        letters = []
        numbers = []
        for element in phrase:
            if element.isalpha():
                letters.append(element)
            else:
                numbers.append(element)
        final_number = int(''.join(numbers))
        first_letter = letters[0]
        last_letter = letters[-1]
        if first_letter.isupper():
            letter_number = char_position(first_letter)
            total_sum += final_number / letter_number
        else:
            letter_number = char_position(first_letter)
            total_sum += final_number * letter_number

        if last_letter.isupper():
            letter_number = char_position(last_letter)
            total_sum -= letter_number
        else:
            letter_number = char_position(last_letter)
            total_sum += letter_number

        final_total_sum += total_sum
    print(f'{final_total_sum:.2f}')


def char_position(letter):
    return ord(letter) - 97


main()
