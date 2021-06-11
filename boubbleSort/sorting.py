

def boubleSort(list):
    n = len(list)
    for j in range(n - 1):
        for i in range(n - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
