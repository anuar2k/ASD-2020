import math

class Node:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.pos = None
        self.sum = 1
    
class IntervalSums:
    def __init__(self, n):
        self.bst = bst(0, n - 1, None)
        self.vals = [0] * n
        pass

    def add_sum(self, i, delta):
        pass
    
    def set(self, i, val):
        delta = val - self.vals[i]
        self.vals[i] = val
        self.add_sum(i, delta)

    def find_val(self, bst, i, j, left_bound, right_bound):
        if bst is None:
            return 0
        if (i == left_bound and j <= right_bound) or (i >= left_bound and j == right_bound):
            return bst.sum

        result = 0
        if j < right_bound:
            result += self.find_val(bst.left, i, j, left_bound, bst.pos)
        if i > left_bound:
            result += self.find_val(bst.right, i, j, bst.pos, right_bound)
        return result

    def interval(self, i, j):
        return self.find_val(self.bst, i, j, -math.inf, +math.inf)
    
def bst(left, right, parent):
    result = Node()
    result.parent = parent

    if left > right:
        result.pos = -1
        result.left = None
        result.right = None
    else:
        middle = (left + right) // 2
        result.pos = middle
        result.left = bst(left, middle - 1, result)
        result.right = bst(middle + 1, right, result)
    return result

IS = IntervalSums(4)
IS.set(0, 10)
IS.set(2, -2)
IS.set(3, 1)
print(IS.interval(0, 3))
print(IS.interval(1, 2))