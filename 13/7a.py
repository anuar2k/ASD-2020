class BSTNode:
    def __init__(self, key, val, parent):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.parent = parent

def BSTMin(root):
    while root.left is not None:
        root = root.left
    return root

def Successor(node):
    if node.right is not None:
        return BSTMin(node.right)
    else:
        while node.parent is not None:
            if node.parent.left is node:
                return node.parent
            else:
                node = node.parent
        return None

def Intersection(root1, root2):
    root1 = BSTMin(root1)
    root2 = BSTMin(root2)
    T = 0
    while not (root1 is None or root2 is None):
        if root1.key == root2.key:
            T+=1
            root1 = Successor(root1)
            root2 = Successor(root2)
        elif root1.key < root2.key:
            root1 = Successor(root1)
        else:
            root2 = Successor(root2)
    return T