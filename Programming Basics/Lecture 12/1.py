real_book = str(input())

is_book_found = False

counter = 0
current_book = input()

while current_book != "No More Books":



    if current_book == real_book:
        is_book_found = True
        print(f'You checked {counter} books and found it.')
        break

    counter += 1

    current_book = input()

    if not is_book_found:
        print(f'The book you search is not here!')
        print(f'You checked {counter} books and found it.')



