from time import sleep
def loading_bar(number_input):
    l_b = number_input
    if number_input == 100:
        return print(f'100% Complete!\n [%%%%%%%%%%]')
    else:
        return print(f'{number_input}% [{l_b * "%"}{"." * (100 - l_b)}]\nStill loading ...')


counter = 1
while True:
    sleep(0.25)
    loading_bar(counter)
    counter += 1
    if counter == 100:
        print(f'100% Complete!')
        break