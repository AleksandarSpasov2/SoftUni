n = int(input())

positive_list = []
negative_list = []

for i in range(n):
    num = int(input())

    if num < 0:
        negative_list.append(num)
    else:
        positive_list.append(num)

        