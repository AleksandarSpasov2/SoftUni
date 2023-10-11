size_1 = int(input())
size_2 = int(input())

cake_size = size_1 * size_2




while True:
    piece_count = str(input())
    if piece_count == "STOP":
        print(f'{cake_size} pieces are left.')
        break

    piece = int(piece_count)
    cake_size -= piece

    if cake_size <= 0:
        print(f'No more cake left! You need {abs(cake_size)} pieces more.')
        break



