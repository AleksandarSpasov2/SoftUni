my_list = [1, 2, 3, 4, 4, 4, 5, 5, 6, 10]

clean_list = [num.remove(4) for num in my_list]

print(clean_list)