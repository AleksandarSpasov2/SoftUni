def main():
    exam_results = {}
    languages = {}
    user_input = input().split("-")
    while True:
        if user_input[0] == 'exam finished':
            break

        if user_input[1] == "banned":
            ban_function(user_input, exam_results)

        elif user_input[1] != 'banned':
            add_function(user_input, exam_results, languages)

        user_input = input().split("-")

    print_function(exam_results, languages)


def ban_function(user_input, exam_results):
    username = user_input[0]
    exam_results['ban'] = exam_results[username]
    del exam_results[username]


def add_function(user_input, exam_results, languages):
    username, language, points = user_input[0], user_input[1], int(user_input[2])
    if username not in exam_results:
        exam_results[username] = {language: [points]}
    else:
        if language not in exam_results[username]:
            exam_results[username][language] = [points]
        else:
            exam_results[username][language].append(points)

    if language not in languages:
        languages[language] = 0
    languages[language] += 1


def print_function(exam_results, languages):
    print(f'Results:')
    for key, value in exam_results.items():
        if key != "ban":
            for values in value.values():
                print(f'{key} | {max(values)}')
    print(f'Submissions:')
    for key, value in languages.items():
        print(f'{key} - {value}')


main()
