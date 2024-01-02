

def heapify(arr, n, i):
    largest = i # set the largest as the root
    left = 2 * i + 1 # index of left child
    right = 2 * i + 2 # index of right child

    # check if left child exists and is greater than the root
    if left < n and arr[largest] < arr[left]:
        largest = left

    # check if right child exists and is greater than the largest so far
    if right < n and arr[largest] < arr[right]:
        largest = right
        
    # swap the largest and the root 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

    
def heapSort(arr):
    n = len(arr)

    # Maxheap
    for i in range(n - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)


    
array = [12, 11, 13, 5, 6, 7, 15, 3]
print("Original array:", array)

heapSort(array)
print("Sorted array:", array)
    

