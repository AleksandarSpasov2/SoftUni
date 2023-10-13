snowballs_count = int(input())

calculated_data = 0
highest_value = 0
highest_weight = 0
highest_time = 0
highest_quality = 0

for n in range(snowballs_count):
    weight_snowball = int(input())
    time_for_snowball = int(input())
    quality_snowball = int(input())

    calculated_data = (weight_snowball / time_for_snowball) ** quality_snowball

    if calculated_data > highest_value:
        highest_value = calculated_data
        highest_weight = weight_snowball
        highest_time = time_for_snowball
        highest_quality = quality_snowball

print(f'{highest_weight} : {highest_time} = {highest_value:.0f} ({highest_quality})')
