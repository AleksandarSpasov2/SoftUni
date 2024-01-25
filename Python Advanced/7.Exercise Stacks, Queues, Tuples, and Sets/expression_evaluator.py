from collections import deque

string_expression = input().split()

numbers = deque()
symbols = deque()

for element in string_expression:
    if element.isdigit() or (element[0] == '-' and element[1].isdigit()):
        element = int(element)
        numbers.append(element)
    else:
        while numbers:
            number = numbers.popleft()
            symbol = symbols.popleft()
            if symbol == '-':
                






