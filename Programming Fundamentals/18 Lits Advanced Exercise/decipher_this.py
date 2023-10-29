message_input = input().split()

for word in range(len(message_input)):
    first_word = message_input[0]
    second_word = message_input[1]
    third_word = message_input[2]
    first_word_num = "".join([element for element in first_word if element.isdigit()])
    second_word_num = "".join([element for element in second_word if element.isdigit()])
    third_word_num = "".join([element for element in third_word if element.isdigit()])

    # first_decript = chr(int(first_word))
    # second_decript = chr(int(second_word))
    # third_decript = chr(int(third_word))








