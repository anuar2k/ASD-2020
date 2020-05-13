#Główną ideą algorytmu jest to, że długość najdłuższej ścieżki w drzewie to potencjalnie
#suma dwóch największych długości (różnych) ścieżek idących w dół drzewa - długości ścieżek
#wychodzących od dzieci uzyskujemy poprzez wybór najdłuższej z jej wnuków + długość krawędzi do dziecka.
#Alternatywnie najdłuższą ścieżkę wychodząca od wierzchołka należy "przekazać" wyżej.

#Złożoność wynosi w przybliżeniu O(E) - mamy E wywołań traverse(G) i wynik każdego z nich poprzez dwa porównania
#"spychamy" w dół kolejki dwóch największych długości, poprzez jedno porównanie aktualizujemy wynik całości

class Node:
    def __init__(self):
        #zmienna children jest zbędna, bo child ma informację o swojej długości
        self.child = []

def heavy_path(T):
    longest = 0

    def traverse(G):
        #uzyskujemy dostęp do zmiennej zadeklarowanej w funkcji zewnętrznej
        nonlocal longest

        biggest = 0 #długość najdłuższej ścieżki wychodzącej z dziecka
        second = 0 #długość drugiej najdłuzszej ścieżki wychodzącej z dziecka

        for subtree in G.child:
            #result to długość najdłuższej ścieżki wychodzącej z dziecka
            #tj. najdłuższa z wnuków + długość krawędzi do dziecka
            result = traverse(subtree[0]) + subtree[1]
            #"spychamy" nowy wynik w dół kolejki
            if result > biggest:
                second = biggest
                biggest = result
            elif result > second:
                second = result
        #potencjalnie nadłuższa ścieżka przechodzi przez nasz wierzchołek
        candidate = biggest + second
        if candidate > longest:
            longest = candidate
        #podajemy najdłuższą ścieżkę wychodzącą od nas wyżej
        return biggest

    #bazowe wywołanie naszej funkcji
    traverse(T)

    return longest

A = Node()
B = Node()
C = Node()
A.child = [(B, 5), (C, -1)]

print(heavy_path(A))