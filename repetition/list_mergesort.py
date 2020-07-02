class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def length(nodes):
    result = 0
    while nodes is not None:
        result += 1
        nodes = nodes.next
    return result

def merge_sort(nodes):
    n = length(nodes)

    if n == 1:
        return nodes
    else:
        half = n // 2

        left_list = nodes
        for _ in range(half - 1):
            nodes = nodes.next
        right_list = nodes.next
        nodes.next = None

        left_list = merge_sort(left_list)
        right_list = merge_sort(right_list)

        result = None
        resultLast = None

        while left_list is not None and right_list is not None:
            if left_list.val <= right_list.val:
                if result is None:
                    result = left_list
                    resultLast = left_list
                else:
                    resultLast.next = left_list
                    resultLast = left_list

                left_list = left_list.next
            else:
                if result is None:
                    result = right_list
                    resultLast = right_list
                else:
                    resultLast.next = right_list
                    resultLast = right_list

                right_list = right_list.next

        if left_list is not None:
            resultLast.next = left_list
        if right_list is not None:
            resultLast.next = right_list

        return result

def traverse(nodes):
    if nodes is not None:
        print(nodes.val)
        traverse(nodes.next)

a = Node(2)
b = Node(1)
c = Node(3)
d = Node(7)
e = Node(9)
f = Node(9)
g = Node(7)
h = Node(4)
i = Node(2)
j = Node(0)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h
h.next = i
i.next = j

traverse(merge_sort(a))