def loading_graphic(user_input):
    bar_length = user_input // 10
    dots = 10 - bar_length
    loading = "[" + "%" * bar_length + "." * dots + "]"

    if user_input < 100:
      return f'{user_input}% {loading}\n Still loading...'

    elif user_input == 100:
        return f'100% Complete!\n' + loading



progress_bar = int(input())

result = loading_graphic(progress_bar)
print(result)

