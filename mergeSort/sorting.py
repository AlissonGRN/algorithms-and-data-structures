

def mergeSort(list, start=0, end=None):
    if end is None:
        end = len(list)
    if(end - start > 1):
        half = (end + start) // 2
        mergeSort(list, start, half)
        mergeSort(list, half, end)
        merge(list, start, half, end)


def merge(list, start, half, end):
    left = list[start:half]
    right = list[half:end]
    topLeft, topRight = 0, 0
    for k in range(start, end):

        if topLeft >= len(left):
            list[k] = right[topRight]
            topRight = topRight + 1
        elif topRight >= len(right):
            list[k] = left[topLeft]
            topLeft = topLeft + 1
        elif left[topLeft] < right[topRight]:
            list[k] = left[topLeft]
            topLeft = topLeft + 1
        else:
            list[k] = right[topRight]
            topRight = topRight + 1
