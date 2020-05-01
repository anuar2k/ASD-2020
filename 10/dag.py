class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.n = len(edges)
        self.visited = [False] * self.n
        self.order = [None] * self.n
        self.distance = [None] * self.n
        self.pos = self.n - 1

def topoOrder(graph, v):
    graph.visited[v] = True
    for u in graph.edges[v]:
        if not graph.visited[u[0]]:
            topoOrder(graph, u[0])

    graph.order[graph.pos] = v
    graph.pos -= 1

def dagPath(G):
    graph = Graph(G)
    topoOrder(graph, 0)

    graph.distance[graph.order[0]] = 0
    for v in graph.order:
        for u in graph.edges[v]:
            if graph.distance[u[0]] is None or graph.distance[u[0]] > graph.distance[v] + u[1]:
                graph.distance[u[0]] = graph.distance[v] + u[1]

    return graph.distance[graph.n - 1]

graph = [[(1, 2)], [(2, 3), (3, 1)], [(4, -3)], [(4, -2), (5, 2)], [(5, 2)],[]]

print(dagPath(graph))