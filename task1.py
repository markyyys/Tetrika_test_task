def task(array):
    array = [int(a) for a in array]
    for i, a in enumerate(array):
        if a == 0:
            return i

print(task("111111111110000000000000000"))
