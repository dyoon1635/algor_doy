import sys
input = sys.stdin.readline
MOD = 10 ** 9 + 7

n, m ,k = map(int, input().split())
leaf = []
tree = [0] * (n * 4)
for _ in range(n):
    leaf.append(int(input()))

def init(node, start, end):
    if start == end:
        tree[node] = leaf[start]
    else:
        tree[node] = (init(node * 2, start, (start + end) // 2) \
        * init(node * 2 + 1, (start + end) // 2 + 1, end)) % MOD
    return tree[node]

def subMul(node, start, end, left, right):
    if left > end or right < start: return 1
    if start >= left and end <= right: return tree[node]
    tmp = subMul(node * 2, start, (start + end) // 2, left, right) * \
        subMul(node * 2 + 1, (start + end) // 2 + 1, end, left, right)
    return tmp % MOD

def update(node, start, end, index, value):
    if index < start or index > end: return
    if start == end: tree[node] = value
    else:
        update(node * 2, start, (start + end) // 2, index, value)
        update(node * 2 + 1, (start + end) // 2 + 1, end, index, value)
        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD

init(1, 0, n - 1)
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        leaf[b - 1] = c
        update(1, 0, n - 1, b - 1, c)
    elif a == 2:
        print(subMul(1, 0, n - 1, b - 1, c - 1))