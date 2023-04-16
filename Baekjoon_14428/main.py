import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = [leaf[start], start]
    else:
        tree[node] = min(init(node * 2, start, (start + end) // 2),
                         init(node * 2 + 1, (start + end) // 2 + 1, end))
    return tree[node]

def sub_query(node, start, end, left, right):
    if start > right or end < left: return base
    if left <= start and end <= right: return tree[node]
    return min(sub_query(node * 2, start, (start + end) // 2, left, right),
               sub_query(node * 2 + 1, (start + end) // 2 + 1, end, left, right))

def update(node, start, end, index, value):
    if index < start or index > end: return
    if start == end:
        tree[node][0] = value
        return tree[node]
    update(node * 2, start, (start + end) // 2, index, value)
    update(node * 2 + 1, (start + end) // 2 + 1, end, index, value)
    tree[node] = min(tree[node * 2], tree[node * 2 + 1])

n = int(input())
leaf = list(map(int, input().split()))
base = [sys.maxsize, sys.maxsize]
tree = [[0, i] for i in range(n * 4)]
m = int(input())
init(1, 0, n - 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        leaf[b - 1] = c
        update(1, 0, n - 1, b - 1, c)
    elif a == 2:
        print(sub_query(1, 0, n - 1, b - 1, c - 1)[1] + 1)