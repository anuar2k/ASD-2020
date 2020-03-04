# znaleźć min i max w tablicy robiąc tylko 1.5n porównań (vs. 2n)

def _min(a, b):
    return a if a < b else b

def _max(a, b):
    return a if a > b else b
     
def minMax(arr):
    n = len(arr)

    # przypisujemy pierwszy element tablicy do min/max
    minVal = arr[0]
    maxVal = arr[0]

    # może zostać nam nieparzysta liczba elementów do porównania, wtedy
    # jeden element musimy potraktować oddzielnie
    if (n - 1) % 2 == 1:
        startPos = 2

        if arr[1] > maxVal:
            maxVal = arr[1]
        if arr[1] < minVal:
            minVal = arr[1]
    else:
        startPos = 1

    for i in range(startPos, n, 2):
        # 0.5n porównań przy wejściu do if'a
        # 1n porównań wewnątrz if'a
        if arr[i] < arr[i + 1]:
            minVal = _min(minVal, arr[i])
            maxVal = _max(maxVal, arr[i + 1])
        else:
            minVal = _min(minVal, arr[i + 1])
            maxVal = _max(maxVal, arr[i])

    return minVal, maxVal

#-------------------------------------------

test1 = [1, 2, 3, 4, 5, 6, 7]
test2 = [2, 1, 3, 7, 4, 2, 0, 9, 9, 7]
test3 = [5]
test4 = [6, 7]
test5 = [7, 8, 9]

print('min: %d, max: %d' % minMax(test1))
print('min: %d, max: %d' % minMax(test2))
print('min: %d, max: %d' % minMax(test3))
print('min: %d, max: %d' % minMax(test4))
print('min: %d, max: %d' % minMax(test5))
