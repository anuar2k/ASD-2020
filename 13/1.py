class BSTNode:
    def __init__(self, key, val, parent):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.parent = parent

# this is a dummy function
def find(root, key):
    return BSTNode()

def succ(root, key):
    root = find(root, key)
    if(root.right):
        root = root.right
        while root.left:
            root = root.left
        return root
    else:
        while root.parent:
            parent = root.parent
            if parent.left == root:
                return parent
            root = parent
    return None
 
 
def pred(root, key):
    root = find(root, key)
    if(root.left):
        root = root.left
        while root.right:
            root = root.right
        return root
    else:
        while root.parent:
            parent = root.parent
            if parent.right == root:
                return parent
            root = parent
    return None