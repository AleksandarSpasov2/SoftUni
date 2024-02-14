from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption = deque([int(x) for x in input().split()])
fuel_needed = deque([int(x) for x in input().split()])

altitude = 0

while initial_fuel and additional_consumption:

    last_fuel = initial_fuel[-1]
    first_additional = additional_consumption[0]
    first_needed = fuel_needed[0]

    if last_fuel - first_additional >= first_needed:
        initial_fuel.pop()
        additional_consumption.popleft()
        fuel_needed.popleft()
        altitude += 1
        print(f"John has reached: Altitude {altitude}")

    else:
        print(f"John did not reach: Altitude {altitude + 1}")
        break

if altitude > 1:
    print(f"John failed to reach the top.\n"
          f" Reached altitudes: {f'Altitude{[x for x in range(1, altitude + 1)]}'}")
else:
    print("John failed to reach the top."
          "John didn't reach any altitude.")

if not initial_fuel and not additional_consumption:
    print("John has reached all the altitudes and managed to reach the top!")
