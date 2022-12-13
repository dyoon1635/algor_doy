import sys

n = int(input())
adj = []
for _ in range(n):
    adj.append(list(map(int, sys.stdin.readline().split())))

edges = []
for i in range(n):
    for j in range(i + 1, n):
        edges.append([i, j, adj[i][j]])

edges.sort(key=lambda x: x[2])
parent = [i for i in range(n + 1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a, b = find(x), find(y)
    parent[b] = a

result = 0
for each in edges:
    a, b, c = each

    if find(a) != find(b):
        union(a, b)
        result += c
print(result)