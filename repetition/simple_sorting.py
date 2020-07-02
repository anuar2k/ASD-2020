# proste algorytmy sortujące O(n^2)

def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selectionSort(arr):
    n = len(arr)

    for i in range(n - 1):
        minIdx = i

        for j in range(i + 1, n):
            if arr[j] < arr[minIdx]:
                minIdx = j

        arr[i], arr[minIdx] = arr[minIdx], arr[i]

def insertionSort(arr):
    n = len(arr)
    
    for i in range(1, n):
        to_insert = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > to_insert:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = to_insert
        
#-------------------------------------------

arr = [2, 1, 3, 7, 4, 2, 0, 9, 9, 7]

arrCopy = arr.copy()
bubbleSort(arrCopy)
print(arrCopy)

arrCopy = arr.copy()
selectionSort(arrCopy)
print(arrCopy)

arrCopy = arr.copy()
insertionSort(arrCopy)
print(arrCopy)
