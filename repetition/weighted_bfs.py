class Node:
    def __init__(self):
        self.next = None
        self.val = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, x):
        N = Node()
        N.val = x

        if self.head is None:
            self.head = N
            self.tail = N
        else:
            self.head.next = N
            self.head = N

    def dequeue(self):
        N = self.tail
        self.tail = self.tail.next

        if self.tail is None:
            self.head = None

        return N.val

    def is_empty(self):
        return self.head is None

def weighted_bfs(graph, source, target):
    q = Queue()

    q.enqueue((source, 0, 0, None))

    parent = [None] * len(graph)
    visited = [False] * len(graph)

    while not q.is_empty():
        v, dist_left, depth, src = q.dequeue()

        if dist_left == 0:
            parent[v] = src
            visited[v] = True
            
            if v == target:
                return depth, parent

            for u in range(len(graph)):
                if not visited[u] and graph[v][u] is not None:
                    q.enqueue((u, graph[v][u], depth, v))
        else:
            # we might've reached vertex v earlier by other, shorter path
            # so we should remove any left instances of v from the queue
            if parent[v] is None:
                q.enqueue((v, dist_left - 1, depth + 1, src))

    return None, parent

graph1 = [
    [None,    3,    2, None],
    [3   , None,    2,    1],
    [2   ,    2, None,    2],
    [None,    1,    2, None]
]

graph2 = [
    [None,    1, None,    5,   10, None],
    [   1, None,    2,    1,    4,    2],
    [None,    2, None, None,    3,    1],
    [   5,    1, None, None,   10, None],
    [  10,    4,    3,   10, None,    2],
    [None,    2,    1, None,    2, None]
]

graph3 = [
    [None,    1,    1,    2, None],
    [   1, None, None,    1, None],
    [   1, None, None,    1, None],
    [   2,    1,    1, None,    1],
    [None, None, None,    1, None]
]

graph4 = [
    [None,    1,    1,   10,   10,   10,   10,   10],
    [   1, None, None,   10,   10,   10,   10,   10],
    [   1, None, None,   10,   10,   10,   10,   10],
    [  10,   10,   10, None, None, None, None, None],
    [  10,   10,   10, None, None, None, None, None],
    [  10,   10,   10, None, None, None, None, None],
    [  10,   10,   10, None, None, None, None, None],
    [  10,   10,   10, None, None, None, None, None],
]

print(weighted_bfs(graph1, 0, 3))
print(weighted_bfs(graph1, 3, 0))
print(weighted_bfs(graph2, 0, 4))
print(weighted_bfs(graph2, 4, 0))
print(weighted_bfs(graph3, 0, 4))
print(weighted_bfs(graph3, 4, 0))
print(weighted_bfs(graph4, 0, 5))
print(weighted_bfs(graph4, 7, 4))
