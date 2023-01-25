import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find(x):
    if x == parent[x]: return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a, b = find(x), find(y)
    if a < b:
        parent[b] = a
        groupsize[a] += groupsize[b]
    else:
        parent[a] = b
        groupsize[b] += groupsize[a]

n, m = map(int, input().split())
edge = []
parent = [i for i in range(n + 1)]
groupsize = [1 for _ in range(n + 1)]
totalCost, cost = 0, 0
for _ in range(m):
    x, y, w = map(int, input().split())
    edge.append((x, y, w))
    totalCost += w
edge.sort(key=lambda x: -x[2])

MOD = 10 ** 9
for x, y, w in edge:
    a, b = find(x), find(y)
    if a != b:
        cost += (totalCost * groupsize[a] * groupsize[b])
        union(x, y)
    totalCost -= w
print(cost % MOD)