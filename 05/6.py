# Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T. Proszę podać algorytm, który oblicza minimalną ilość monet potrzebną
# do wydania kwoty T (algorytm zachłanny nie działa)

# M = [1, 3, 4, 7]
# m = len(M)

# F = [None] * (m + 1)

# f(t) - najmniejsza liczba monet niezbedna do wydania wartosci t
# f(0) = 0
# f(t) = infinity, t < 0
# f(t) = min({f(t - M[i]) + 1: i=1,2..m})

import math

def change(amount, cache, monetary_system):
    if amount < 0:
        return math.inf
    if amount == 0:
        return 0
    if cache[amount - 1] is not None:
        return cache[amount - 1]

    result = math.inf

    for bill in monetary_system:
        result = min(result, change(amount - bill, cache, monetary_system) + 1)
    
    cache[amount - 1] = result
    return cache[amount - 1]

amount = 10
monetary_system = [3, 6, 3, 9, 2, 4]
cache = []
for _ in range(amount):
    cache.append(None)

print(change(amount, cache, monetary_system))