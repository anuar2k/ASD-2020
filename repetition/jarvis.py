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

def jarvis(points):
    if len(points) < 4:
        return points

    points.sort(key=functools.cmp_to_key(rightmosthighest_cmp))
    result = [points[0]]
    points = points[1:]

    while True:
        points.sort(key=functools.cmp_to_key(angle_cmp(result[-1])))
        to_add = points[0]
        points = points[1:]
        if to_add == result[0]:
            break
        result.append(to_add)

    return result

# TODO: FIX ME PLS
print(jarvis([(-2, -2), (-2, 2), (2, -2), (-2, -2), (-1, -1), (1, 1), (-1, 1), (1, -1), (0, 0)]))