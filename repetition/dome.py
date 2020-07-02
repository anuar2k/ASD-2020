import math

def cover(x, domes):
    domes_by_end = [[] for _ in range(x + 1)]

    for dome in domes:
        if dome[1] <= x:
            domes_by_end[dome[1]].append(dome)

    cost = [math.inf] * (x + 1)
    cost[0] = 0

    for i in range(1, x + 1):
        for dome in domes_by_end[i]:
            new_cost = cost[dome[0] - 1] + dome[2]
            if new_cost < cost[i]:
                cost[i] = new_cost

    return cost[x]

print(cover(5, [(1, 1, 3), (2, 3, 3), (1, 3, 7), (4, 5, 2)]))