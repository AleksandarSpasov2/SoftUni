def main():
    main_dict = {}

    while True:
        resource = input()
        if resource == "stop":
            break
        quantity = int(input())

        if resource not in main_dict:
            main_dict[resource] = 0
        main_dict[resource] += quantity

    print_function(main_dict)


def print_function(main_dict):
    for key, value in main_dict.items():
        print(f'{key} -> {value}')


main()
