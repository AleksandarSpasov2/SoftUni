my_dict = {"name": "Alex", "age": 44}

print(my_dict)

my_dict["phone"] = +359787456

print(my_dict)

my_dict["phone"] = None

print(my_dict)

for key, value in my_dict.items():
    print("Key", key)
    print("Value", value)
    print()