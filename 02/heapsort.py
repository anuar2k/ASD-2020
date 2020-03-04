def heapify(arr, size, pos):
    maximum = pos
    lChild = pos * 2 + 1
    rChild = pos * 2 + 2

    if (lChild < size and arr[lChild] > arr[maximum]):
        maximum = lChild

    if (rChild < size and arr[rChild] > arr[maximum]):
        maximum = rChild

    if (maximum != pos):
        arr[pos], arr[maximum] = arr[maximum], arr[pos]
        heapify(arr, size, maximum)

def buildHeap(arr, size):
    for idx in range((size // 2) - 1, -1, -1):
        heapify(arr, size, idx)

def heapSort(arr):
    n = len(arr)

    buildHeap(arr, n)

    for idx in range(n - 1, 0, -1):
        arr[0], arr[idx] = arr[idx], arr[0]
        heapify(arr, idx, 0)

    return arr
    
#-------------------------------------------

print(heapSort([5, 7, 4, 2, 1, 3, 6]))