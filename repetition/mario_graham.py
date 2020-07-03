from sys import maxsize as maxInt
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return 'x: ' + str(self.x) + ' y: ' + str(self.y)
 
def getStartPoint(points):
    minx = maxInt
    miny = maxInt
    for i in range(len(points)):
        if points[i].y <= miny:
            if points[i].y < miny:
                res = i
                miny = points[i].y
                minx = points[i].x
            else:
                if points[i].x < minx:
                    res = i
                    minx = points[i].x
    return res
 
def distanceBetweenPoints(p1, p2):
    return ((p1.x-p2.x)**2+(p1.y-p2.y)**2)
 
def partition(A, l, p, p0):
    i = l - 1
    pivot = p
    for j in range(l, p):
        if orientation(p0, A[pivot], A[j]) == -1:
            i += 1
            A[i], A[j] = A[j], A[i]
    i += 1
    A[i], A[pivot] = A[pivot], A[i]
    return i
 
 
def quickSort(A, l, p, p0):
    if p > l:
        pivot = partition(A, l, p, p0)
        quickSort(A, l, pivot - 1, p0)
        quickSort(A, pivot + 1, p, p0)
 
def orientation(p1, p2, p3):
    val = ((p2.y - p1.y) * (p3.x - p2.x)) - ((p2.x - p1.x) * (p3.y - p2.y))
    if (val > 0):
        # Clockwise orientation
        return -1
    elif (val < 0):
        # Counterclockwise orientation
        return 1
    else:
        if distanceBetweenPoints(p1, p2) > distanceBetweenPoints(p1, p3):
            return -1
        else:
            return 1
 
def leftOrRight(p1, p2, p3):
    val = ((p2.y - p1.y) * (p3.x - p2.x)) - ((p2.x - p1.x) * (p3.y - p2.y))
    if (val > 0):
        # Clockwise orientation
        return -1
    elif (val < 0):
        # Counterclockwise orientation
        return 1
    else:
        return 0
 
 
def graham(points):
    p0 = getStartPoint(points)
    points[0], points[p0] = points[p0], points[0]
    p0 = points[0]
    points2 = points[1:]
    quickSort(points2, 0, len(points2) - 1, p0)
    stack = [p0, points2[0], points2[1]]
 
    for i in range(1, len(points2)):
        while len(stack) > 1:
            d = leftOrRight(stack[len(stack) - 2], stack[len(stack) - 1], points2[i])
            if d >= 0:
                break
            else:
                stack.pop()
        stack.append(points2[i])
    return stack

points = [Point(-1, -1), Point(0, 0), Point(1, 1), Point(-1, 1), Point(1, -1), Point(0, 1), Point(1, 0), Point(-1, 0), Point(0, -1)]
res = graham(points)
for i in res:
    print(i.x, i.y)