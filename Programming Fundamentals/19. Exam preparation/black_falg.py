days_of_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

plunder = 0

for day in range(1, days_of_plunder + 1):
    plunder += daily_plunder

    if day % 3 == 0:
        plunder += 0.5 * daily_plunder

    if day % 5 == 0:
        plunder -= 0.3 * plunder

if plunder >= expected_plunder:
    print(f'Ahoy! {plunder:.2f} plunder gained.')
    
else:
    difference = plunder / expected_plunder * 100
    print(f'Collected only {difference:.2f}% of the plunder.')


