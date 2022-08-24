import sys

n, m, k = map(int, sys.stdin.readline().split())
leaf = []
tree = [0] * 3000000
for _ in range(n):
    leaf.append(int(sys.stdin.readline()))

def init(node, start, end):
    if start == end:
        tree[node] = leaf[start]
        return tree[node]
    else:
        tree[node] = init(node * 2, start, (start + end) // 2) \
                     + init(node * 2 + 1, (start + end) // 2 + 1, end)
        return tree[node]

# node 구간 : [start, end]
# sum 구간  : [left, right]
def subSum(node, start, end, left, right):
    if left > end or right < start: return 0
    if start >= left and end <= right: return tree[node]
    return subSum(node * 2, start, (start + end) // 2, left, right) \
           + subSum(node * 2 + 1, (start + end) // 2 + 1, end, left, right)

def update(node, start, end, index, diff):
    if index < start or index > end: return
    tree[node] += diff
    if start != end:
        update(node * 2, start, (start + end) // 2, index, diff)
        update(node * 2 + 1, (start + end) // 2 + 1, end, index, diff)

init(1, 0, n - 1)
for _ in range(m + k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        diff = c - leaf[b - 1]
        leaf[b - 1] = c
        update(1, 0, n - 1, b - 1, diff)
    elif a == 2:
        print(subSum(1, 0, n - 1, b - 1, c - 1))