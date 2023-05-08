import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def find(x):
    if x == parent[x]: return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    parent[max(px, py)] = min(px, py)

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
for count in range(1, m + 1):
    a, b = map(int, input().split())
    if find(a) != find(b): union(a, b)
    else:
        print(count)
        exit(0)
print(0)
