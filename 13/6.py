class BNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def sumValues(T):
    result = 0

    curr = T
    prev = None

    while curr is not None:
        if prev == curr.parent:
            result += curr.value
            prev = curr
            if curr.left is not None:
                curr = curr.left
            elif curr.right is not None:
                curr = curr.right
            else:
                curr = curr.parent
        elif prev == curr.left:
            prev = curr
            if curr.right is not None:
                curr = curr.right
            else:
                curr = curr.parent
        else:
            prev = curr
            curr = curr.parent

    return result