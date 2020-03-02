# sprawdź, czy żadne zadane dwa przedziały czasu się nie przecinają
# zakładamy, że przedziały czasu są liczbami całkowitymi

# sortuje okresy czasu wg początku okresu (przez zliczanie), jednocześnie sprawdzając,
# czy nie ma dwóch okresów o takim samym początku - wtedy też się przecinają
def countingSort(arr):
    minStartTime = arr[0][0]
    maxStartTime = arr[0][1]

    for time in arr:
        if (time[0] < minStartTime):
            minStartTime = time[0]
        if (time[0] > maxStartTime):
            maxStartTime = time[0]
    
    histSize = maxStartTime - minStartTime + 1

    hist = []
    for i in range(0, histSize):
        hist.append(None)
    
    for time in arr:
        idx = time[0] - minStartTime
        if (hist[idx] is None):
            hist[idx] = time
        else:
            # znaleźliśmy dwa okresy o tym samym początku, na ogół jest to
            # zbędne sprawdzenie, ale upraszcza ono sam algorytm sortujący,
            # bo nie musimy w hist trzymać tablicy tupli, a same pojedyncze
            return True
    
    idx = 0
    for i in range(0, histSize):
        if (hist[i] is not None):
            arr[idx] = hist[i]
            idx = idx + 1
    
    return False
        
def overlap(arr):
    if (not countingSort(arr)):
        n = len(arr)
        for i in range(n - 1):
            if (arr[i][1] > arr[i + 1][0]):
                return True
        
        return False
    else:
        return True

#-------------------------------------------

test1 = [(3, 4), (5, 6), (1, 2)]            # nie przecinają się
test2 = [(1, 2), (3, 4), (1, 2)]            # takie same początki
test3 = [(1, 3), (5, 8), (4, 6)]            # koniec[i] > początek[i + 1]
test4 = [(1, 5), (6, 11), (30, 50), (5, 6)] # nie przecinają się

print(overlap(test1))
print(overlap(test2))
print(overlap(test3))
print(overlap(test4))

print()
print(test1)
print(test2) # nieposortowane, bo występują takie same początki
print(test3)
print(test4)