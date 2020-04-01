# Dana jest szachownica A o wymiarach n x n. Szachownica zawiera liczby wymierne. Należy przejść z pola (1,1) na pole (n,n) najmniejszym kosztem. A[x][y] - koszt.

# cost(x, y) = A[x][y] + min(cost(x - 1, y), cost(x, y - 1))
# cost(0, 0) = A[0][0]
# cost(0, y) = A[0][y] + cost(0, y - 1)
# cost(x, 0) = A[x][0] + cost(x - 1, 0)

def cost(A, lookup, x, y):
    if lookup[x][y] is not None:
        return lookup[x][y]

    if x == 0 and y == 0:
        lookup[x][y] = A[x][y]
        return lookup[x][y]

    if x == 0:
        lookup[x][y] = A[x][y] + cost(A, lookup, x, y - 1)
        return lookup[x][y]
    if y == 0:
        lookup[x][y] = A[x][y] + cost(A, lookup, x - 1, y)
        return lookup[x][y]

    lookup[x][y] = A[x][y] + min(cost(A, lookup, x - 1, y), cost(A, lookup, x, y - 1))
    return lookup[x][y]
    
def costIter(A):
    lookup = []
    for x in range(len(A)):
        lookup.append([])
        for y in range(len(A)):
            if x == 0 and y == 0:
                lookup[x].append(A[x][y])
                continue
            if x == 0:
                lookup[x].append(A[x][y] + lookup[x][y - 1])
                continue
            if y == 0:
                lookup[x].append(A[x][y] + lookup[x - 1][y])
                continue
            
            lookup[x].append(A[x][y] + min(lookup[x - 1][y], lookup[x][y - 1]))

    return lookup[len(A) - 1][len(A) - 1]

A = [[1, 2, 3, 4], \
     [1, 2, 3, 4], \
     [1, 2, 3, 4], \
     [1, 2, 3, 4]]

lookup = []

for i in range(len(A)):
    lookup.append([])
    for j in range(len(A)):
        lookup[i].append(None)

print(cost(A, lookup, len(A) - 1, len(A) - 1))
print(costIter(A))
