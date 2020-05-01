class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

    def __repr__(self):
        return f"{self.source} -> {self.target}"

class Vertex:
    def __init__(self):
        self.parent = self
        self.rank = 0

class VertexSets:
    def __init__(self, size):
        self.size = size
        self.vertices = [Vertex() for x in range(size)]

    def __find_set(self, x):
        if x is not x.parent:
            x.parent = self.__find_set(x.parent)
        return x.parent

    def __merge(self, x, y):
        x = self.__find_set(x)
        y = self.__find_set(y)
        if x.rank > y.rank:
            y.parent = x
        else:
            x.parent = y
            if x.rank == y.rank:
                y.rank += 1

    def union(self, x, y):
        self.__merge(self.vertices[x], self.vertices[y])
        
    def same_set(self, x, y):
        return self.__find_set(self.vertices[x]) is self.__find_set(self.vertices[y])

def kruskal(graph):
    n = len(graph)
    edges = []
    for source in range(n):
        for pair in graph[source]:
            if pair[0] > source:
                edges.append(Edge(source, pair[0], pair[1]))

    edges.sort(key=lambda edge: edge.weight)
    sets = VertexSets(n)

    result = []
    for edge in edges:
        if not sets.same_set(edge.source, edge.target):
            result.append(edge)
            sets.union(edge.source, edge.target)

    return result

graph = [[(1, 3), (5, 2)], 
         [(2, 1), (6, 2)], 
         [(1, 1), (3, 7)], 
         [(2, 7), (6, 5), (4,8)], 
         [(3, 8), (5, 6)], 
         [(0, 2), (6, 1), (4, 6)], 
         [(1, 2), (3, 5), (5, 1)]]

print(kruskal(graph))
