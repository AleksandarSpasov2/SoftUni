matrix = []

# for j in range(0, 3):
#     sub_list = []
#     for i in range(0, 2):
#         sub_list.append(0)
#     matrix.append(sub_list)
#
# print(matrix)

for j in range(3):
    matrix.append([])
    for i in range(2):
        matrix[j].append(0)
print(matrix)