def loading_bar(progress):
    bar_length = progress // 10
    loading = "[" + "%" * bar_length + "." * (10 - bar_length) + "]"

    if progress < 100:
        return f"{progress}% {loading}\nStill loading..."
    else:
        return "100% Complete!\n" + loading


# Get the input
input_number = int(input("Enter a number between 0 and 100 (divisible by 10): "))

# Check if the input is within the valid range
if 0 <= input_number <= 100 and input_number % 10 == 0:
    result = loading_bar(input_number)
    print(result)
else:
    print("Invalid input. Please enter a number between 0 and 100 divisible by 10.")
