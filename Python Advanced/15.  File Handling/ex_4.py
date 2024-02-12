import os
try:
    path = os.path.join('my_fist_file.txt')
    os.remove(path)
except FileNotFoundError:
    print('File not found')
