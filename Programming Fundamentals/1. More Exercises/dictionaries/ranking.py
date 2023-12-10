def contest_password():
    contest_dict = {}
    contest_input = input()

    while contest_input != 'end of contests':
        contest, password_for_contest = contest_input.split(':')
        if contest not in contest_dict.keys():
            contest_dict[contest] = password_for_contest
        contest_dict[contest] += password_for_contest
        contest_input = input()
