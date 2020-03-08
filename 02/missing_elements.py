# w tablicy zawierającej n elementów (parami różnych) znajdź dla przedziału [low, high] takie liczby, które są w tym przedziale, ale nie ma ich w tablicy. O(n)

def findMissing(arr, low, high):
    n = len(arr)
    minVal = arr[0]
    maxVal = arr[0]

    for idx in range(1, n):
        if arr[idx] < minVal:
            minVal = arr[idx]
        if arr[idx] > maxVal:
            maxVal = arr[idx]

    histSize = maxVal - minVal + 1
    hist = [False] * histSize

    for val in arr:
        hist[val - minVal] = True

    result = []

    for idx in range(low, high + 1):
        if not hist[idx - minVal]:
            result.append(idx)

    return result

#-------------------------------------------

print(findMissing([-3, 8, 4, 5, 6], 1, 7))