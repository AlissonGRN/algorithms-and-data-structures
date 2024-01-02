
def linearSearch(arr, value):

    for i in range(len(arr)):
        if arr[i] == value:
            return i # return the position if the value is found
    return -1 # return -1 if the value is not found
