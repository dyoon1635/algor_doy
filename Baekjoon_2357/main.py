import sys
from math import *

sys.setrecursionlimit(int(1e+6))
n ,m = map(int, sys.stdin.readline().split())
leaf = []
h = int(ceil(log2(n)))
t_size = 1 << (h + 1)
min_tree = [0] * t_size
max_tree = [0] * t_size
for _ in range(n):
    leaf.append(int(sys.stdin.readline()))

def initMin(node, start, end):
    if start == end:
        min_tree[node] = leaf[start]
        return min_tree[node]
    mid = (start + end) // 2
    min_tree[node] = min(initMin(node * 2, start, mid),
                         initMin(node * 2 + 1, mid + 1, end))
    return min_tree[node]

def initMax(node, start, end):
    if start == end:
        max_tree[node] = leaf[start]
        return max_tree[node]
    mid = (start + end) // 2
    max_tree[node] = max(initMax(node * 2, start, mid),
                         initMax(node * 2 + 1, mid + 1, end))
    return max_tree[node]

def minQuery(node, start, end, left, right):
    if end < left or start > right: return 1000000001
    if left <= start and end <= right: return min_tree[node]
    mid = (start + end) // 2
    return min(minQuery(node * 2, start, mid, left, right),
               minQuery(node * 2 + 1, mid + 1, end, left, right))

def maxQuery(node, start, end, left, right):
    if end < left or start > right: return 0
    if left <= start and end <= right: return max_tree[node]
    mid = (start + end) // 2
    return max(maxQuery(node * 2, start, mid, left, right),
               maxQuery(node * 2 + 1, mid + 1, end, left, right))
initMin(1, 0, n - 1)
initMax(1, 0, n - 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(minQuery(1, 0, n - 1, a - 1, b - 1),
          maxQuery(1, 0, n - 1, a - 1, b - 1))