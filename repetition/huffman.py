class PriorityQueue:
    def __init__(self, init_size):
        self.__size = 0
        self.__heap = [None] * init_size

    def __lchild(self, idx):
        return idx * 2 + 1

    def __rchild(self, idx):
        return idx * 2 + 2

    def __parent(self, idx):
        return (idx - 1) // 2

    def __heapify(self, pos):
        maximum = pos
        lChild = self.__lchild(pos)
        rChild = self.__rchild(pos)

        if lChild < self.__size and self.__heap[lChild] < self.__heap[maximum]:
            maximum = lChild

        if rChild < self.__size and self.__heap[rChild] < self.__heap[maximum]:
            maximum = rChild

        if maximum != pos:
            self.__heap[pos], self.__heap[maximum] = self.__heap[maximum], self.__heap[pos]
            self.__heapify(maximum)

    def extract_min(self):
        if self.__size == 0:
            raise Exception("The queue is empty")

        result = self.__heap[0]

        self.__heap[0] = self.__heap[self.__size - 1]
        self.__size -= 1
        self.__heapify(0)

        return result

    def insert(self, x):
        self.__size += 1

        if self.__size > len(self.__heap):
            self.__heap.append(x)
        else:
            self.__heap[self.__size - 1] = x
        
        pos = self.__size - 1
        while pos > 0 and self.__heap[self.__parent(pos)] > self.__heap[pos]:
            self.__heap[self.__parent(pos)], self.__heap[pos] = self.__heap[pos], self.__heap[self.__parent(pos)]
            pos = self.__parent(pos)

    def size(self):
        return self.__size

class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.val < other.val

def huffman_len(A):
    pq = PriorityQueue(len(A))

    for count in A:
        pq.insert(Node(count, None, None))

    while pq.size() > 1:
        a = pq.extract_min()
        b = pq.extract_min()
        pq.insert(Node(a.val + b.val, a, b))

    result = 0

    def traverse(node, depth):
        nonlocal result
    
        if node.left is None and node.right is None:
            result += node.val * depth
        else:
            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)

    traverse(pq.extract_min(), 0)

    return result

print(huffman_len([200, 700, 180, 120, 70, 30]))
