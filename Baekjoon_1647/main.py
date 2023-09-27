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
parent = [i for i in range(n + 1)]
pq = []
for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(pq, (c, a, b))

result = 0
ex_w = 0
while pq:
    w, a, b = heapq.heappop(pq)
    pa, pb = find(a), find(b)

    if pa != pb:
        result += w
        union(pa, pb)
        ex_w = w
print(result - ex_w)

