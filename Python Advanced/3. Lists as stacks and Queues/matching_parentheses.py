expression = input()

new_expression = []

for index in range(len(expression)):
    if expression[index] == '(':
        new_expression.append(index)

    elif expression[index] == ')':
        start_index = new_expression.pop()
        end_index = index + 1
        print(expression[start_index:end_index])


