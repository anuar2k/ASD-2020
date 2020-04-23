# złącz k posortowanych tablic mających razem n elementów w czasie O(nlogk)

class HeapObj:
    def __init__(self, arr):
        self.arr = arr
        self.__head = 0

    def head(self):
        return self.arr[self.__head]

    def pop(self):
        result = self.head()
        self.__head += 1
        return result

    def isEmpty(self):
        return self.__head == len(self.arr)

    def __lt__(self, right):
        if right.isEmpty():
            return True
        if self.isEmpty():
            return False

        return self.head() < right.head()

def heapify(heap, size, pos):
    minimum = pos
    lChild = pos * 2 + 1
    rChild = pos * 2 + 2

    if lChild < size and heap[lChild] < heap[minimum]:
        minimum = lChild

    if rChild < size and heap[rChild] < heap[minimum]:
        minimum = rChild

    if minimum != pos:
        heap[pos], heap[minimum] = heap[minimum], heap[pos]
        heapify(heap, size, minimum)

def buildHeap(heap):
    size = len(heap)
    for idx in range((size // 2) - 1, -1, -1):
        heapify(heap, size, idx)

def mergeArrays(values):
    heap = []
    n = 0

    for value in values:
        heap.append(HeapObj(value))
        n += len(value)
    
    buildHeap(heap)

    result = []

    for _ in range(n):
        result.append(heap[0].pop())
        heapify(heap, len(heap), 0)

    return result

print(mergeArrays([[1, 5, 7], [0], [3, 4, 13], [-2, 8, 9], [0, 1, 10], [-3, 6, 7, 10, 12]]))
