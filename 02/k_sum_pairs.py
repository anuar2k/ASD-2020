# znajdź wszystkie takie pary liczb w tablicy n-elementowej, by dawały one sumę k, O(n)

def movePtr(arr, ptr, direction):
    if direction:
        n = len(arr)
        ptr += 1
        while ptr < n and arr[ptr] == 0:
            ptr += 1
    else:
        ptr -= 1
        while ptr >= 0 and arr[ptr] == 0:
            ptr -= 1

    return ptr

def countKSumPairs(arr, k):
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

    l = 0
    r = histSize - 1

    result = 0

    while l <= r:
        _sum = l + r + (2 * minVal)
        if _sum == k:
            if l == r:
                result += (hist[l] * (hist[l] - 1)) // 2
            else:
                result += hist[l] * hist[r]

            l = movePtr(hist, l, True)
        elif _sum < k:
            l = movePtr(hist, l, True)
        else:
            r = movePtr(hist, r, False)

    return result

#-------------------------------------------

print(countKSumPairs([3, 2, 1, 5, 4, 4, 4, 7, 7, 9, -1], 8))