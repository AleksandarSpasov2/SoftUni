def main():
    company_dict = {}
    command = input()

    while command != "End":
        company, id = command.split(" -> ")

        if company not in company_dict.keys():
            company_dict[company] = [id]
        else:
            company_dict[company].append(id)

        command = input()

    print_function(company_dict)


def print_function(company_dict):
    for key, value in company_dict.items():
        print(key)
        for element in value:
            print(f'--{element}')


main()
