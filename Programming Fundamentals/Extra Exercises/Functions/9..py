def palindrome_function(string_input):
    is_palindrome = False
    if string_input == string_input[::-1]:
        is_palindrome = True

    return is_palindrome


word_input = "abaa"
print(palindrome_function(word_input))
