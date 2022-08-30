import sys
from math import *

n, m = map(int, sys.stdin.readline().split())
h = int(ceil(log2(n)))
t_size = 1 << (h + 1)
leaf = []
tree = [0] * t_size
for _ in range(n):
    leaf.append(int(sys.stdin.readline()))

def init(node, start, end):
    if start == end:
        tree[node] = leaf[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = min(init(node * 2, start, mid),
                     init(node * 2 + 1, mid + 1, end))
    return tree[node]

def Query(node, start, end, left, right):
    if start > right or end < left: return sys.maxsize
    if left <= start and end <= right: return tree[node]
    mid = (start + end) // 2
    return min(Query(node * 2, start, mid, left, right),
               Query(node * 2 + 1, mid + 1, end, left, right))


init(1, 0, n - 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(Query(1, 0, n - 1, a - 1, b - 1))