# pylint: disable=unused-wildcard-import
from inttree import *

def intervals(I):
    result = [I[0][1] - I[0][0]]
    edges = [edge for tpl in I for edge in tpl]

    edges = sorted(edges)

    uniq_edges = [edges[0]]

    for edge in edges:
        if edge != uniq_edges[len(uniq_edges) - 1]:
            uniq_edges.append(edge)
    T = tree(uniq_edges)
    tree_insert(T, I[0])

    for i in range(1, len(I) - 1):
        res = result[i - 1]
        new_span = I[i]
        tree_insert(T, new_span)

        left = tree_intersect(T, new_span[0])
        if len(left) == 2:
            a = min(left[0][0], left[1][0])
            b = max(left[0][1], left[1][1])
            tree_remove(T, left[0])
            tree_remove(T, left[1])

            if b - a > res:
                res = b - a

            tree_insert(T, (a, b))

        right = tree_intersect(T, new_span[1])
        if len(right) == 2:
            a = min(right[0][0], right[1][0])
            b = max(right[0][1], right[1][1])
            tree_remove(T, right[0])
            tree_remove(T, right[1])

            if b - a > res:
                res = b - a

            tree_insert(T, (a, b))
        result.append(res)

    return result

run_tests(intervals)
