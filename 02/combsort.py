def getSpan(span):
    span = span * 10 // 13
    return span if span >= 1 else 1

def getSpan11(span):
    span = span * 10 // 13

    if (span == 9 or span == 10):
        span = 11

    return span if span >= 1 else 1

def combSort(arr, eleven = False):
    n = len(arr)
    span = n
    swapped = True
    nextSpan = getSpan11 if eleven else getSpan

    while span > 1 or swapped:
        span = nextSpan(span)
        swapped = False
        for idx in range(0, n - span):
            if arr[idx] > arr[idx + span]:
                arr[idx], arr[idx + span] = arr[idx + span], arr[idx]
                swapped = True

    return arr

#-------------------------------------------

print(combSort([5, 4, 3, 2, 1]))
print(combSort([3, 4, 5, 2, 1], True))

