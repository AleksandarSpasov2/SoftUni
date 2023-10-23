def reverse_string(input_string):
    reversed_string = ""
    for index in range(len(input_string)-1, -1, -1):
        reversed_string += input_string[index]

    return reversed_string

input_str = input()
print(reverse_string(input_str))