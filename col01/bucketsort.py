import math, random

class Node:
    def __init__(self):
        self.value = None
        self.next = None

def last(nodes):
    if nodes is not None:
        while nodes.next is not None:
            nodes = nodes.next
    
    return nodes

def length(nodes):
    count = 0
    while nodes is not None:
        nodes = nodes.next
        count += 1
    return count

def bucketSort(nodes, low = 0, high = 10):
    n = length(nodes)

    if n <= 1:
        return nodes

    step = (high - low) / n
    buckets = [None] * n

    for _ in range(n):
        buckIdx = math.floor((nodes.value - low) / (high - low) * n)
        node = nodes
        nodes = nodes.next
        node.next = buckets[buckIdx]
        buckets[buckIdx] = node

    for i in range(n):
        buckets[i] = bucketSort(buckets[i], low + step * i, low + step * (i + 1))

    resultFirst = None
    resultLast = None
    for i in range(n):
        if buckets[i] is not None:
            if resultFirst is None:
                resultFirst = buckets[i]
                resultLast = last(buckets[i])
            else:
                resultLast.next = buckets[i]
                resultLast = last(buckets[i])

    return resultFirst

random.seed(0)
for _ in range(10):
    nodes = None
    for _ in range(10):
        node = Node()
        node.value = random.uniform(0, 10)
        node.next = nodes
        nodes = node

    nodes = bucketSort(nodes)
    while nodes is not None:
        print(f"{nodes.value:.5f}", end=" ")
        nodes = nodes.next
    print("")
