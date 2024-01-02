

def selectionSort(list):

    n = len(list)
    for j in range(n - 1):
        minIndex = j
        for i in range(j, n):
            if list[i] < list[minIndex]:
                minIndex = i

        if list[j] > list[minIndex]:
            aux = list[j]
            list[j] = list[minIndex]
            list[minIndex] = aux
