import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find(x):
    if parent[x] <= 0: return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px != py:
        parent[px] += parent[py]
        parent[py] = px

n, l = map(int, input().split())
parent = [-1 for i in range(300001)]
for _ in range(n):
    a, b = map(int, input().split())

    if parent[find(a)] + parent[find(b)] < 0:
        union(a, b)
        parent[find(a)] += 1
        print('LADICA')
    else: print('SMECE')