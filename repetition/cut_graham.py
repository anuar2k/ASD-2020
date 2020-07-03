import functools
import math
# otoczka wypukła

def rightmosthighest_cmp(p1, p2):
    return p1[1] - p2[1] if p1[1] != p2[1] else p1[0] - p2[0]

def cross_product(p1, p2):
    return p1[0] * p2[1] - p2[0] * p1[1]

def clockwiseness(p0, p1, p2):
    p1 = (p1[0] - p0[0], p1[1] - p0[1])
    p2 = (p2[0] - p0[0], p2[1] - p0[1])
    return cross_product(p1, p2)

def angle_cmp(p0):
    def point_clockwiseness(p1, p2):
        return clockwiseness(p0, p1, p2)

    return point_clockwiseness

def graham(points):
    if len(points) < 4:
        return points

    lowest = min(points, key=functools.cmp_to_key(rightmosthighest_cmp))
    ordered = sorted(points, key=functools.cmp_to_key(angle_cmp(lowest)))

    result = []

    for point in ordered:
        while len(result) >= 2 and clockwiseness(result[-2], result[-1], point) > 0:
            result.pop()
        result.append(point)

    return result

print(graham([(-1, -1), (0, 0), (1, -1), (1, 1), (-1, 1), (0, 1), (1, 0), (-1, 0), (0, -1)]))