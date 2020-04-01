# TODO: reimplement everything

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.freq = 0

def heapify(arr, size, pos):
    minimum = pos
    lChild = pos * 2 + 1
    rChild = pos * 2 + 2

    if lChild < size and arr[lChild].freq < arr[minimum].freq:
        minimum = lChild

    if rChild < size and arr[rChild].freq < arr[minimum].freq:
        minimum = rChild

    if minimum != pos:
        arr[pos], arr[minimum] = arr[minimum], arr[pos]
        heapify(arr, size, minimum)

def parent(i):
    return (i - 1) // 2

def buildHeap(arr, size):
    for idx in range((size // 2) - 1, -1, -1):
        heapify(arr, size, idx)

def extractMin(arr, size):
    minimum = arr[0]
    arr[0] = arr[size - 1]
    size -= 1
    heapify(arr, size, 0)
    return minimum

def heapDecreaseKey(arr, i, key):
    arr[i] = key
    while i > 0 and arr[parent(i)].freq > arr[i].freq:
        arr[i], arr[parent(i)] = arr[parent(i)], arr[i]
        i = parent(i)

def insert(arr, key, size):
    size += 1
    arr[size - 1] = 10000000
    heapDecreaseKey(arr, size - 1, key)

def huffman_len(A):
    n = len(A)
    size = n
    for i in range(n):
        node = Node()
        node.freq = A[i]
        A[i] = node

    for i in range(2 * n):
        A.append(None)

    buildHeap(A, size)
    for _ in range(n - 1):
        z = Node()
        z.left = extractMin(A, size)
        z.right = extractMin(A, size)
        z.freq = z.left.freq + z.right.freq
        insert(A, z, size)

    return A

x = huffman_len([200, 700, 180, 120, 70, 3])