first_input = input().split(", ")
second_input = int(input())

money_list = []

for current_money in first_input:
    money_list.append(int(current_money))

final_sums = []

star_index = 0

while star_index < second_input:
    current_beggar_sum = 0
    for current_index in range(star_index, len(money_list), second_input):
        current_beggar_sum += money_list[current_index]
    final_sums.append(current_beggar_sum)
    star_index += 1

print(final_sums)

