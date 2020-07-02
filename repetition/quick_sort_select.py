import random

def partition(T, low, high):
    pivot = random.randint(low, high)
    T[high], T[pivot] = T[pivot], T[high]

    split = low
    for i in range(low, high):
        if T[i] < T[high]:
            T[i], T[split] = T[split], T[i]
            split += 1

    T[split], T[high] = T[high], T[split]
    return split

def quickSelect(T, low, high, n):
    while low < high:
        pivot = partition(T, low, high)
        if pivot == n:
            return T[pivot]
        if pivot < n:
            low = pivot + 1
        else:
            high = pivot - 1

    return T[low]

def quickSort(T, low, high):
    if low < high:
        pivot = partition(T, low, high)
        
        if pivot - low < high - pivot:
            quickSort(T, low, pivot - 1)
            low = pivot + 1
        else:
            quickSort(T, pivot + 1, high)
            high = pivot - 1


    