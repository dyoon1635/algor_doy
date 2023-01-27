import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def find(x):
    if x == parent[x]: return x
    tmp = find(parent[x])
    weight[x] += weight[parent[x]]
    parent[x] = tmp
    return parent[x]

def union(x, y, w):
    if x > y:
        x, y, w = y, x, -w
    a, b = find(x), find(y)
    if a == b: return

    weight[b] = weight[x] - weight[y] + w
    parent[b] = a

while True:
    n, m = map(int, input().split())
    if not n and not m: break

    parent = [i for i in range(n + 1)]
    weight = [0 for _ in range(n + 1)]
    for _ in range(m):
        tmp = input().strip().split()
        if tmp[0] == '!':
            a, b, w = map(int, tmp[1:])
            union(a, b, w)
        else:
            a, b = map(int, tmp[1:])
            print(weight[b] - weight[a] if find(a) == find(b) else 'UNKNOWN')
