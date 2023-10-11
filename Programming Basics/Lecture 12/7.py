free_space_w = int(input())
free_space_l = int(input())
free_space_h = int(input())

total_free_sapce = free_space_w * free_space_l * free_space_h
total_taken_space = 0

while True:
    boxes = str(input())

    if boxes == "Done":
        diff_2 = abs(total_free_sapce - total_taken_space)
        print(f'{diff_2} Cubic meters left.')
        break

    num_boxes = int(boxes)
    total_taken_space += num_boxes
    if total_taken_space >= total_free_sapce:
        diff = abs(total_taken_space - total_free_sapce)
        print(f'No more free space! You need {diff} Cubic meters more.')
        break
