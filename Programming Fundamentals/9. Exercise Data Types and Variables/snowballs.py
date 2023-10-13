snowballs_count = int(input())

highest_value = 0
calculated_data = 0

weight_snowball = int(input())
time_for_snowball = int(input())
quality_snowball = int(input())

for n in range(snowballs_count):

    calculated_data = (weight_snowball / time_for_snowball) ** quality_snowball

    if calculated_data > highest_value:
        highest_value = calculated_data

print(f'{weight_snowball} : {time_for_snowball} = {highest_value:.0f} ({quality_snowball})')
