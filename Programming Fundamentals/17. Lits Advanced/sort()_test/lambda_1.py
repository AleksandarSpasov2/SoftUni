
my_list = ["a-10", "b-2", "c-5"]

sorted_list = sorted(my_list, key=lambda x: int(x.split("-")[1]))

