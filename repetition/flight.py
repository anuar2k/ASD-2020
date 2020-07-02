import math

class Interval:
    def __init__(self, interval=None):
        self.intervals = []
        if interval is not None:
            self.intervals.append(interval)

    def __add__(self, other):
        intervals_sum = []

        intervals_sum += self.intervals
        intervals_sum += other.intervals

        result = Interval()
        result.intervals = intervals_sum
        return result

    def __mul__(self, other):
        intervals_inter = []

        for a in self.intervals:
            for b in other.intervals:
                if b[0] <= a[1] and b[1] >= a[0]:
                    intervals_inter.append((max(a[0], b[0]), min(a[1], b[1])))

        result = Interval()
        result.intervals = intervals_inter
        return result

def flight(matrix, source, target, t):
    v = [Interval() for _ in range(len(matrix))]
    v[source] = Interval((-math.inf, +math.inf))

    for _ in range(len(matrix) - 1):
        for src in range(len(matrix)):
            for tgt in range(len(matrix)):
                if matrix[src][tgt] is not None:
                    v[tgt] = v[tgt] + (v[src] * Interval((matrix[src][tgt] - t, matrix[src][tgt] + t)))

    ##################################################################
    # TODO: Improve __add__ and __mul__, find computational complexity
    ##################################################################
    print(len(v[target].intervals))

    return len(v[target].intervals) > 0

matrix = [
    [None, 7, 5, None, None],
    [7, None, None, 5, None],
    [5, None, None, 12, 10],
    [None, 5, 12, None, 8],
    [None, None, 10, 8, None]
]

print(flight(matrix, 0, 4, 2))
