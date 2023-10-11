

year = int(input())

is_special = False

year_to_be_checked = year

while not is_special:
    year_to_be_checked += 1
    year_to_be_checked_as_str = str(year_to_be_checked)
    is_special = True

    for index in year_to_be_checked_as_str:
        if year_to_be_checked_as_str.count(index) > 1:
            is_special = False
            break

print(year_to_be_checked)