def calculation_function(action: str, num_1: int, num_2: int):
    if action == "multiply":
        result = num_1 * num_2
        return print(result)
    elif action == "divide":
        result = int(num_1 / num_2)
        return print(result)
    elif action == "add":
        result = num_1 + num_2
        return print(result)
    elif action == "subtract":
        result = num_1 - num_2
        return print(result)


action = str(input())
num_1_input = int(input())
num_2_input = int(input())
calculation_function(action, num_1_input, num_2_input)