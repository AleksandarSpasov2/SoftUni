my_dict = {'a': 1, 'b': 2}

try:
    print(my_dict['b'])
except KeyError:
    print("Not a valid key")
finally:
    print('Try Again')
