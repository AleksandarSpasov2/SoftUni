def calculate_damage(price_r, entry_p, type_i):
    rate = list(map(int, price_r.split(", ")))
    entry_value = rate[entry_p]

    if type_i == "cheap":
        left_values = [x for x in rate[:entry_p] if x < entry_value]
        right_values = [x for x in rate[entry_p+1:] if x < entry_value]
    else:
        left_values = [x for x in rate[:entry_p] if x >= entry_value]
        right_values = [x for x in rate[entry_p+1:] if x >= entry_value]

    left_sum = sum(left_values)
    right_sum = sum(right_values)

    if left_sum >= right_sum:
        return f"Left - {left_sum}"
    else:
        return f"Right - {right_sum}"


user_inp_price_r = input()
user_inpt_entry_p = int(input())
user_inp_type_i = input().strip()

print(calculate_damage(user_inp_price_r, user_inpt_entry_p, user_inp_type_i))
