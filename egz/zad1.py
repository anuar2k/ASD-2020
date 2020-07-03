# Ponieważ koszty danych krawędzi są dość niskie (do 8) możemy pokusić się, aby użyć "ważonego BFS'a".
# Ważony BFS, podobnie jak zwykły, znajduje najkrótsze ściezki do wierzchołka startowego, z tym, że jeśli
# wyjmie on krawędź z kolejki o pozostałej długości do pokonania, to tą długość dekrementuje i wstawia z powrotem.
# Dodatkowo problemem w zadaniu jest to, że po dojściu do każdego wierzchołka na 3 sposoby musimy wybrać inną metodę,
# więc każdy docelowy wierzchołek będzie mieć swój koszt inny dla każdej metody docelowej użytej dla niego.

# Złożoność BFS'a to ok. O(V^2) (dla repr. macierzowej) - w tym przypadku dla każdej krawędzi wysłanie nowego przebiegu po niej możemy zrobić
# dwukrotnie, ponieważ np. dla krawędzi lotniczej mogliśmy wcześniej dotrzeć do jej początku mostem lub statkiem.
# Dodatkowo, każdy przebieg jest przetwarzany wielokrotnie, ale o maksymalnie 8 (stałą ilość) razy, więc te dwa współczynniki
# nie powodują (przemnożenie przez stałą) zwiększenia złożoności algorytmu.

import math

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

def cost_to_method(cost):
    method = [None, 0, None, None, None, 1, None, None, 2]
    return method[cost]

def islands(G, A, B):
    q = Queue()

    q.enqueue((A, None, 0, 0))

    cost = [[math.inf] * 3 for _ in range(len(G))]

    while not q.is_empty():
        v, method, dist_left, new_cost = q.dequeue()

        if dist_left == 0:
            if method is None or new_cost < cost[v][method]:
                if method is None:
                    cost[v][0] = new_cost
                    cost[v][1] = new_cost
                    cost[v][2] = new_cost
                else:
                    cost[v][method] = new_cost

                for u in range(len(G)):
                    new_method = cost_to_method(G[v][u])

                    if new_method is not None and new_method != method and cost[u][new_method] == math.inf:
                        q.enqueue((u, new_method, G[v][u], new_cost + G[v][u]))
        else:
            if cost[v][method] > new_cost:
                q.enqueue((v, method, dist_left - 1, new_cost))

    result = math.inf
    for result_cost in cost[B]:
        if result_cost < result:
            result = result_cost

    return result
