
countries_dict = {}


countries = input().split(", ")
capitals = input().split(", ")
final_result = {countries[index]: capitals[index] for index in range(len(countries))}

for key, value in final_result.items():
    print(f'{key} -> {value}')

