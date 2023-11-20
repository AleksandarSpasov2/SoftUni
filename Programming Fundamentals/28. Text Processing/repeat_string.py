def main():
    string_input = input().split()
    result = ""
    for word in string_input:
        lenght = len(word)
        result += word * lenght

    print(result)


main()
