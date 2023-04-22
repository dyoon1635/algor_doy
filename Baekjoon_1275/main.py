import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = leaf[start]
    else:
        tree[node] = init(node * 2, start, (start + end) // 2) + \
                     init(node * 2 + 1, (start + end) // 2 + 1, end)
    return tree[node]

def subSum(node, start, end, left, right):
    if start > right or end < left: return 0
    if left <= start and end <= right: return tree[node]
    return subSum(node * 2, start, (start + end) // 2, left, right) + \
           subSum(node * 2 + 1, (start + end) // 2 + 1, end, left, right)

def update(node, start, end, index, value):
    if index < start or index > end: return
    tree[node] += value
    if start != end:
        update(node * 2, start, (start + end) // 2, index, value)
        update(node * 2 + 1, (start + end) // 2 + 1, end, index, value)

n, q = map(int, input().split())
leaf = list(map(int, input().split()))
tree = [0 for _ in range(n * 4)]
init(1, 0, n - 1)
for _ in range(q):
    x, y, a, b = map(int, input().split())
    if x > y: x, y = y, x

    print(subSum(1, 0, n - 1, x - 1, y - 1))
    diff = b - leaf[a - 1]
    leaf[a - 1] = b
    update(1, 0, n - 1, a - 1, diff)

