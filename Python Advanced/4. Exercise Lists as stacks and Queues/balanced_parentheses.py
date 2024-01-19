from collections import deque

parentheses_input = input()

opening_p = deque()


for element in parentheses_input:
    if element == '(' or element == '{' or element == '[':
        opening_p.append(element)

    else:
        corresponding_element = opening_p.pop()
        if corresponding_element == '(' and element == ')':
            continue
        elif corresponding_element == '[' and element == ']':
            continue
        elif corresponding_element == '{' and element == '}':
            continue
        else:
            print(f'NO')
            break

if not opening_p:
    print(f'YES')