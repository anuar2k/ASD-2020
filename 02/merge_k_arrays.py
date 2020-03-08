# złącz k posortowanych tablic mających razem n elementów w czasie O(nlogk)

def headValue(values, arrHeads, arrIdx):
    return values[arrIdx][arrHeads[arrIdx]]

def listEmpty(arrHeads, valSizes, arrIdx):
    return arrHeads[arrIdx] == valSizes[arrIdx]

def heapify(idxHeap, arrHeads, values, valSizes, size, pos):
    minimum = pos
    lChild = pos * 2 + 1
    rChild = pos * 2 + 2

    if lChild < size:
        if (listEmpty(arrHeads, valSizes, idxHeap[minimum])
            or (not listEmpty(arrHeads, valSizes, idxHeap[lChild])
                and headValue(values, arrHeads, idxHeap[lChild]) < headValue(values, arrHeads, idxHeap[minimum]))):
            minimum = lChild

            
    if rChild < size:
        if (listEmpty(arrHeads, valSizes, idxHeap[minimum])
            or (not listEmpty(arrHeads, valSizes, idxHeap[rChild])
                and headValue(values, arrHeads, idxHeap[rChild]) < headValue(values, arrHeads, idxHeap[minimum]))):

            minimum = rChild

    if minimum != pos:
        idxHeap[pos], idxHeap[minimum] = idxHeap[minimum], idxHeap[pos]
        heapify(idxHeap, arrHeads, values, valSizes, size, minimum)

def buildHeap(idxHeap, arrHeads, values, valSizes, size):
    for idx in range((size // 2) - 1, -1, -1):
        heapify(idxHeap, arrHeads, values, valSizes, size, idx)

def mergeArrays(values):
    k = len(values)
    n = 0
    idxHeap = []
    arrHeads = [0] * k
    valSizes = []

    for idx in range(k):
        valSizes.append(len(values[idx]))
        n += len(values[idx])
        idxHeap.append(idx)

    buildHeap(idxHeap, arrHeads, values, valSizes, k)

    result = []

    for _ in range(n):
        result.append(headValue(values, arrHeads, idxHeap[0]))
        arrHeads[idxHeap[0]] += 1
        heapify(idxHeap, arrHeads, values, valSizes, k, 0)

    return result

print(mergeArrays([[1, 5, 7], [0], [3, 4, 13], [-2, 8, 9], [0, 1, 10], [-3, 6, 7, 10, 12]]))