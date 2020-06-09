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

    for i in range(1, len(I)):
        res = max(result[i - 1], I[i][1] - I[i][0])
        new_span = I[i]
        tree_insert(T, new_span)

        left = tree_intersect(T, new_span[0])
        if len(left) > 1:
            a = min([tup[0] for tup in left])
            b = max([tup[1] for tup in left])
            for tup in left:
                tree_remove(T, tup)

            if b - a > res:
                res = b - a

            tree_insert(T, (a, b))

        right = tree_intersect(T, new_span[1])
        if len(right) > 1:
            a = min([tup[0] for tup in left])
            b = max([tup[1] for tup in left])
            for tup in left:
                tree_remove(T, tup)

            if b - a > res:
                res = b - a

            tree_insert(T, (a, b))
        result.append(res)

    return result

run_tests(intervals)
