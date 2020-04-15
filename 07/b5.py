from collections import deque

class List:
    def __init__(self, val, nex):
        self.value = val
        self.next = nex

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
    
    def put(self, val):
        if self.is_empty():
            self.first = List(val, None)
            self.last = self.first
        else:
            self.last.next = List(val, None)
            self.last = self.last.next

    def get(self):
        tmp = self.first
        self.first = self.first.next
        return tmp.value
        
    def is_empty(self):
        return self.first == None

def czy_dwudzielny(G):
    queue = Queue()

    color = [None]*len(G)
    color[0] = True
    queue.put(0)

    while queue.is_empty() == False:
        node = queue.get()
        for v in G[node]:
            if v != node:
                if color[v] == None:
                    queue.put(v)
                    color[v] = not color[node]
                elif color[v] == color[node]:
                    return False
    
    return True

def czy_jest_cykl(G):
    queue = Queue()

    color = [None] * len(G)
    prev = [None] * len(G)
    color[0] = True
    queue.put(0)

    while queue.is_empty() == False:
        node = queue.get()
        for v in G[node]:
            if prev[node] != v and v != node:
                if color[v] == None:
                    queue.put(v)
                    color[v] = True
                    prev[v] = node
                else:
                    return True
    
    return False

G = [[1,2],[0,3],[0,3], [2,1]]
print( czy_dwudzielny(G) )
print( czy_jest_cykl(G))
