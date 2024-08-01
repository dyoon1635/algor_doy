import sys, math
input = sys.stdin.readline

def init(start, end, idx):
    if start == end:
        tree[idx] = leaf[start]
        return
    mid = (start + end) // 2
    init(start, mid, idx * 2)
    init(mid + 1, end, idx * 2 + 1)
    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]

def update(start, end, idx, node, value):
    if start <= node <= end:
        tree[idx] += value
        if start == end:
            return
        mid = (start + end) // 2
        update(start, mid, idx * 2, node, value)
        update(mid + 1, end, idx * 2 + 1, node, value)

def search(start, end, idx, left, right):
    if start > right or end < left:
        return 0
    if left <= start and end <= right:
        return tree[idx]
    mid = (start + end) // 2
    return search(start, mid, idx * 2, left, right) + \
           search(mid + 1, end, idx * 2 + 1, left, right)


for _ in range(int(input())):
    n, m = map(int, input().split())
    leaf = [0] * m + [1] * n
    pos = [0] + [m + i for i in range(n)]
    MAX = 2 ** (math.ceil(math.log2(m + n)) + 1)

    tree = [0 for _ in range(MAX)]
    init(0, m + n - 1, 1)

    step = list(map(int, input().split()))
    tmp = m - 1
    for each_step in step:
        update(0, m + n - 1, 1, pos[each_step], -1)
        print(search(0, m + n - 1, 1, 0, pos[each_step] - 1), end=' ')
        pos[each_step] = tmp
        tmp -= 1
        update(0, m + n - 1, 1, pos[each_step], 1)
    print('')
