def print_dict(main_dict):
    for key, value in main_dict.items():
        print(f'{key} -> {value}')


main_dict = {}

while True:
    resource = input()
    if resource == 'stop':
        break
    quantity = int(input())

    if resource not in main_dict.keys():
        main_dict[resource] = 0
    main_dict[resource] += quantity

print_dict(main_dict)