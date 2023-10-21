def grades_function(grade_input_func: float):
    if 2.00 <= grade_input_func <= 2.99:
        return print("Fail")
    elif 3.00 <= grade_input_func <= 3.49:
        return print("Poor")
    elif 3.50 <= grade_input_func <= 4.49:
        return print("Good")
    elif 4.50 <= grade_input_func <= 5.49:
        return print("Very Good")
    elif 5.50 <= grade_input_func <= 6.00:
        return print("Excellent")


grade_input = float(input())
grades_function(grade_input)

