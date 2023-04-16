import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = leaf[start]
    else:
        tree[node] = min(init(node * 2, start, (start + end) // 2),
                         init(node * 2 + 1, (start + end) // 2 + 1, end))
    return tree[node]

def sub_query(node, start, end, left, right):
    if left > end or right < start: return base
    if start >= left and end <= right: return tree[node]
    return min(sub_query(node * 2, start, (start + end) // 2, left, right),
               sub_query(node * 2 + 1, (start + end) // 2 + 1, end, left, right))

def update(node, start, end, index, value):
    if start > index or end < index: return
    if start == end:
        tree[node] = value
        return
    update(node * 2, start, (start + end) // 2, index, value)
    update(node * 2 + 1, (start + end) // 2 + 1, end, index, value)
    tree[node] = min(tree[node * 2], tree[node * 2 + 1])

n = int(input())
leaf = list(map(int, input().split()))
base = max(leaf)
tree = [0] * (n * 4)
m = int(input())
init(1, 0, n - 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        leaf[b - 1] = c
        update(1, 0, n - 1, b - 1, c)
    elif a == 2:
        print(sub_query(1, 0, n - 1, b - 1, c - 1))