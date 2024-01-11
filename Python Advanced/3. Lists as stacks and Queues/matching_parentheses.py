user_input = input()

result = ''
inside_parentheses = False

for element in user_input:
    if inside_parentheses:
        if element == ')':
            break
        result += element
    elif element == '(':
        inside_parentheses = True

print(result)
