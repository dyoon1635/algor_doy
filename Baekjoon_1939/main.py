import sys, heapq
input = sys.stdin.readline

def find(x):
    if x == parent[x]: return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px != py:
        parent[max(px, py)] = min(px, py)

n, m = map(int, input().split())
pq = []
parent = [i for i in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(pq, (-c, a, b))
x, y = map(int, input().split())

while pq:
    c, a, b = heapq.heappop(pq)
    union(a, b)
    if find(x) == find(y):
        print(-c)
        break