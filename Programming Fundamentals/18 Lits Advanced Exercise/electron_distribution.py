number_of_electrons = int(input())
shells = []

for shell in range(1, number_of_electrons + 1):
    max_electro_in_current = 2 * shell ** 2
    if number_of_electrons >= max_electro_in_current:
        shells.append(max_electro_in_current)
        number_of_electrons -= max_electro_in_current
        if number_of_electrons == 0:
            break
    else:
        shells.append(number_of_electrons)
        break

print(shells)


