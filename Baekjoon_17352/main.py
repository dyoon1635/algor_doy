import sys
sys.setrecursionlimit(100000)

n = int(input())
parent = [i for i in range(n + 1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a, b = find(x), find(y)
    parent[b] = a

for _ in range(n - 2):
    x, y = map(int, sys.stdin.readline().split())
    union(x, y)

for i in range(1, n + 1):
    if i == parent[i]:
        print(i, end=' ')