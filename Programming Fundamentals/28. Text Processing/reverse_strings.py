def main():

    while True:
        string_input = input()
        if string_input == "end":
            break
        reverse_string = string_input[::-1]
        print_function(string_input, reverse_string)


def print_function(string_input, reverse_string):
    print(f'{string_input} = {reverse_string}')


main()