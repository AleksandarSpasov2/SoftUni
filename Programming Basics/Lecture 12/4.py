


while True:
    steps = str(input())
    total_steps = 0
    total_steps_2 = 0
    total_steps_3 = 0

    if steps == "Going home":
        num_steps_2 = int(input())
        total_steps_2 += num_steps_2
        total_steps_3 += total_steps
        total_steps_3 += total_steps_2

        if total_steps >= 10000:
            print(f'Goal reached! Good job')
            print(f'{total_steps_3 - 10000} steps over the goal!')
            break
        if total_steps < 10000:
            print(f'{10000 - total_steps_3} more steps to reach goal')
            break

    num_steps = int(steps)
    total_steps += num_steps

    if total_steps >= 10000:
        print(f'Goal reached! Good job')
        print(f'{total_steps - 10000} steps over the goal!')
        break

