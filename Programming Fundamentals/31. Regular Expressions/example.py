import re


def regex_function(regex, string):
    match = re.search(regex, string)

    if match:
        print('Match Found', match.group())
    else:
        print('No match found')


regex_function('\d', 'Ivan88')
