import sys, heapq
input = sys.stdin.readline

def find(x):
    if x == parent[x]: return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    parent[max(px, py)] = min(px, py)

v, e = map(int, input().split())
pq = []
for _ in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(pq, (c, a, b))
parent = [i for i in range(v + 1)]

result = 0
while pq:
    c, a, b = heapq.heappop(pq)
    if find(a) == find(b): continue
    union(a, b)
    result += c
print(result)