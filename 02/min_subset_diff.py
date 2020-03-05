# znajdź minimalną różnicę elementu minimalnego i maksymalnego w k-elementowych podzbiorach tablicy n-elementowej, O(n)

def countingSort(arr):
    n = len(arr)
    minVal = arr[0]
    maxVal = arr[0]

    for idx in range(1, n):
        if arr[idx] < minVal:
            minVal = arr[idx]
        if arr[idx] > maxVal:
            maxVal = arr[idx]

    histSize = maxVal - minVal + 1
    hist = [0] * histSize

    for val in arr:
        hist[val - minVal] += 1
    
    idx = 0
    for i in range(histSize):
        while hist[i] > 0:
            arr[idx] = i + minVal
            hist[i] -= 1
            idx += 1
    
    return arr


def minSubSetDiff(arr, k):
    n = len(arr)
    if (k > n):
        raise ValueError("k musi być <= n")

    countingSort(arr)

    minDiff = arr[k - 1] - arr[0]
    for i in range(1, n - k + 1):
        diff = arr[i + k - 1] - arr[i]
        if (diff < minDiff):
            minDiff = diff

    return minDiff

#-------------------------------------------

print(minSubSetDiff([1, 6, 6, 3], 3))