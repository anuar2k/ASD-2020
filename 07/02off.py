# << UWAGA UWAGA UWAGA >>
# << UWAGA UWAGA UWAGA >>
# << UWAGA UWAGA UWAGA >>

# ponieważ nie byłem pewien, czy implementacja DFS z zadania ma obsługiwać dodatkowo pola entry/process
# jak w implementacji z wykładu (są one zbędne do realizacji wymaganego wyniku), to napisałem dwie wersje
# programu - zwykłą (implementującą zapis czasu wejścia i zakończenia przetwarzania wierzchołka) jak i 
# okrojoną (z dopiskiem Raw)

# komentarze do kodu pojawią się tylko w pierwszej wersji

# ----------------------------------------
# wersja z obsługą entry/process z wykładu
# ----------------------------------------

# klasa przechowujące informacje o wierzchołkach
class Vertex:
    def __init__(self):
        self.visited = False
        self.parent = None
        self.entry = None
        self.process = None

# ponieważ wybrałem wersję bez funkcji wewnątrz funkcji, to DFSVisit musi przyjmować dodatkowe argumenty
# jak i zwracać time, by w kolejnych wywołaniach rekurencyjnych ten czas mógł być aktualizowany
def DFSVisit(G, vertices, time, u):
    time += 1
    vertices[u].visited = True
    vertices[u].entry = time

    # reprezentacja macierzy pozwala nam uzyskać sąsiadów przez proste odwołanie do G[u]
    for v in G[u]:
        if not vertices[v].visited:
            vertices[v].parent = u
            # przypisujemy time, gdyż nie mamy globalnego licznika
            time = DFSVisit(G, vertices, time, v)

    time += 1
    vertices[u].process = time
    # zwracamy czas, jaki upłynął w danym wywołaniu rekurencyjnym
    return time

def DFS(G):
    n = len(G)
    time = 0
    vertices = []
    # tworzymy listę obiektów zawierających informacje o wierzchołkach
    for _ in range(n):
        vertices.append(Vertex())

    for v in range(n):
        if not vertices[v].visited:
            # przypisujemy time, gdyż nie mamy globalnego licznika
            time = DFSVisit(G, vertices, time, v)

    # ponieważ informacje o każdym z wierzchołków mamy w tablicy z bezpośrednim dostępem, wystarczy ją przejśc liniowo
    result = []
    for vertex in vertices:
        result.append(vertex.parent)
    return result

# ----------------------------------------------------------------------------
# wersja okrojona, zawierająca tylko to, co jest potrzebne do uzyskania wyniku
# ----------------------------------------------------------------------------

class VertexRaw:
    def __init__(self):
        self.visited = False
        self.parent = None

def DFSVisitRaw(G, vertices, u):
    vertices[u].visited = True
    
    for v in G[u]:
        if not vertices[v].visited:
            vertices[v].parent = u
            DFSVisitRaw(G, vertices, v)

def DFSRaw(G):
    n = len(G)
    vertices = []
    for _ in range(n):
        vertices.append(VertexRaw())

    for v in range(n):
        if not vertices[v].visited:
            DFSVisitRaw(G, vertices, v)

    result = []
    for vertex in vertices:
        result.append(vertex.parent)
    return result
            
# przykłady użycia
G = [[1,2],[0,2,3],[3,1,0],[]]

print(DFS(G))
print(DFSRaw(G))