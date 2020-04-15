class Node:
    def __init__(self):
        self.next = None
        self.val = None

# kolejka na odsyłaczach bez wartownika
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, x):
        N = Node()
        N.val = x

        # w przypadku, gdy nasza kolejka jest pusta musimy zarówno ustawić head i tail
        if self.head is None:
            self.head = N
            self.tail = N
        else:
            self.head.next = N
            self.head = N

    def dequeue(self):
        N = self.tail
        self.tail = self.tail.next

        # w przypadku, gdy usunęliśmy ostatni element z ogona, to głowa nadal wskazuje na ostatni element - też trzeba go usunąć
        if self.tail is None:
            self.head = None

        return N.val

    def is_empty(self):
        # równie dobrze może być to self.tail is None
        return self.head is None

# klasa opisująca informacje o każdym z wierzchołków, potrzebna do pracy BFS'a
class Vertex:
    def __init__(self):
        self.distance = 0
        self.visited = False
        self.parent = None

# funkcja zwraca listę numerów wierzchołków, do których można dojść z wierzchołka nr source
def neighbours(G, source):
    result = []

    for target in range(len(G[source])):
        # if 0 / if 1 - w Py mamy zjawisko truthiness/falsiness
        if G[source][target]:
            result.append(target)

    return result

def BFS(G, s):
    Q = Queue()
    # tu przechowujemy informacje o odwiedzonych wierzchołkach i ich odległościach od s
    vertices = []

    for _ in range(len(G)):
        vertices.append(Vertex())

    vertices[s].visited = True

    Q.enqueue(s)

    while not Q.is_empty():
        u = Q.dequeue()
        for v in neighbours(G, u):
            if not vertices[v].visited:
                vertices[v].visited = True
                vertices[v].distance = vertices[u].distance + 1
                # zapisujemy numer wierzchołka-rodzica, a nie sam obiekt Vertex by móc łatwo stworzyć tablicę result
                vertices[v].parent = u
                Q.enqueue(v)

    result = []
    for vertex in vertices:
        result.append((vertex.parent, vertex.distance))

    return result

G = [[0,1,1,0],[0,0,0,1],[0,1,0,1],[0,0,0,0]]
print(BFS(G, 0))