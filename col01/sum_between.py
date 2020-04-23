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

def sumBetween(T, low, high):
    n = len(T)
    quickSelect(T, 0, n - 1, low)
    quickSelect(T, low, n - 1, high)
    result = 0
    for i in range(low, high + 1):
        result += T[i]

    return result

T = [2, 1, 3, 7, 4, 2, 0, 6, 9, 1, 7]
print(sumBetween(T, 2, 5))
print(T)