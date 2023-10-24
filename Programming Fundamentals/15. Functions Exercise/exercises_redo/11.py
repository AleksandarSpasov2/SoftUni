from time import sleep
def loading_bar(number_input):
    l_b = number_input
    if number_input == 100:
        return print(f'100% Complete!\n [%%%%%%%%%%]')
    else:
        return print(f'{number_input}% [{l_b * "%"}{"." * (100 - l_b)}]\nStill loading ...')


user_input = int(input())
while True:
    number_to_be = 1
    sleep(1.00)
    loading_bar(number_to_be)
    number_to_be += 1
