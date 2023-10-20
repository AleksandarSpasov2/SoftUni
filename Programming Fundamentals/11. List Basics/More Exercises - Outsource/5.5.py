def list_string(list_input):
    new_list = []
    for index in list_input:
        new_list.append(str(index))
    return new_list
def match_words(words):
    magic_word = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            magic_word += 1
    return magic_word


user_input = [1, 2, "aba", "b"]

user_input_1 = list_string(user_input)
user_input_2 = match_words(user_input_1)
print(user_input_2)
print(user_input_1)