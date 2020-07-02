import math

class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * (self.capacity + 1)
        self.head = 0
        self.tail = 0

    def enqueue(self, x):
        if (self.head - self.tail) % len(self.storage) == self.capacity:
            raise Exception("Queue is full")

        self.storage[self.head] = x
        self.head = (self.head + 1) % len(self.storage)

    def dequeue(self):
        result = self.storage[self.tail]
        self.tail = (self.tail + 1) % len(self.storage)

        return result

    def is_empty(self):
        return self.head == self.tail

def capacity(graph, flow, u, v):
    result = 0

    if graph[u][v] > 0:
        result = graph[u][v] - flow[u][v]
    if graph[v][u] > 0:
        result = flow[v][u]
        
    return result 

def bfs(graph, flow, source, target):
    q = Queue(len(graph))

    q.enqueue((source, None))

    parent_map = [None] * len(graph)
    visited = [False] * len(graph)

    while not q.is_empty():
        u, parent = q.dequeue()
        parent_map[u] = parent
        visited[u] = True
        for v in range(len(graph)):
            if not visited[v] and capacity(graph, flow, u, v) > 0:
                q.enqueue((v, u))

    return parent_map

def max_flow(graph, source, target):
    flow = [[0] * len(graph) for _ in range(len(graph))]

    while (parent_map := bfs(graph, flow, source, target))[target] is not None:
        u = parent_map[target]
        v = target
        min_capacity = math.inf

        while u is not None:
            c = capacity(graph, flow, u, v)

            if c < min_capacity:
                min_capacity = c

            u = parent_map[u]
            v = parent_map[v]

        u = parent_map[target]
        v = target

        while u is not None:
            if graph[u][v] > 0:
                flow[u][v] = flow[u][v] + min_capacity
            else:
                flow[v][u] = flow[v][u] - min_capacity

            u = parent_map[u]
            v = parent_map[v]

    return flow

graph = [
    [0, 80, 10, 0],
    [0, 0, 50, 20],
    [0, 0, 0, 80],
    [0, 0, 0, 0]
]

print(max_flow(graph, 0, 3))