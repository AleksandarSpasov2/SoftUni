def main():
    number_of_pieces = int(input())

    for piece in range(number_of_pieces):
        piece, composer, key = input().split("|")
