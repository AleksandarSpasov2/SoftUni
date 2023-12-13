country_names = input().split(", ")
capital_cities = input().split(", ")

main_dict = dict(zip(country_names, capital_cities))

for key, value in main_dict.items():
    print(f'{key} -> {value}')