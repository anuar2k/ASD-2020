def PauseVisit(G, visited, u, toRemove):
    visited[u] = True

    for v in G[u]:
        if not visited[v]:
            PauseVisit(G, visited, v, toRemove)

    toRemove.append(u)
    return toRemove

def Pause(G):
    return PauseVisit(G, [False] * len(G), 0, [])
            
# przykład użycia
G = [[2, 3], [2], [1, 7, 9, 10, 11], \
     [0, 4, 5, 13], [3], [3], [8, 9], \
     [2, 12, 14], [6, 9], [2, 6, 8], \
     [2], [2], [7], [3], [7]]

print(Pause(G))