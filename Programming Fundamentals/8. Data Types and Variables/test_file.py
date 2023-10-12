name = str(input())

for index, letter in enumerate(name):
    for index_2 in range(index + 1):

        letter = "".join([letter * 3])
        print(letter)

