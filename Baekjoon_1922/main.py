import sys

n, m = int(input()), int(input())
cost = []
parent = [i for i in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    cost.append([a, b, c])
cost.sort(key=lambda x: x[2])

def find(x):
    if x == parent[x]: return x # if root
    return find(parent[x])

def union(x, y):
    parent[find(x)] = find(y)

res = 0
for each in cost:
    a, b, c = each # start, end, cost
    if find(a) == find(b): continue
    res += c
    union(a, b)
print(res)