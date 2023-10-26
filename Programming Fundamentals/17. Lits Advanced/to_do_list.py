def list_task():
    to_do_list = []
    while True:
        note = input()
        if note == "End":
            break

        to_do_list.append(note)
    sorted_list = sorted(to_do_list, key=lambda x: int(x.split("-")[0]))
    return [note.split("-")[1] for note in sorted_list]


print(list_task())