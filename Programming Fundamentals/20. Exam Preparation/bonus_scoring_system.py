def main():
    number_of_students = int(input())
    total_lectures = int(input())
    bonus = int(input())
    final_result = []
    final_attendance = []

    for student in range(number_of_students + 1):
        count_of_attendance = int(input())
        current_bonus = bonus_calculation(count_of_attendance, total_lectures, bonus)
        final_result.append(int(current_bonus))
        final_attendance.append(int(count_of_attendance))

    max_bonus(final_result, final_attendance)
    exit()


def bonus_calculation(count_of_attendance, total_lectures, bonus):
    return count_of_attendance / total_lectures * (5 * bonus)


def max_bonus(final_result, final_attendance):
    max_result = max(final_result)
    index = final_result.index(max_result)
    max_attendance = final_attendance[index]
    print(f"Max Bonus: {max_result}.\nThe student has attended {max_attendance} lectures.")


main()