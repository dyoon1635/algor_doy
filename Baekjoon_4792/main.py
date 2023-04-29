import sys, heapq
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def find(x):
    if x == parent[x]: return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    parent[max(px, py)] = min(px, py)

def kruskal(pq):
    global parent, total_edge
    parent = [i for i in range(n + 1)]
    result = 0
    while pq:
        c, f, t = heapq.heappop(pq)
        if find(f) != find(t):
            total_edge += 1
            result += c
            union(f, t)
    return result

while True:
    n, m, k = map(int, input().split())
    if n == 0: break
    total_edge = 0
    minBlue, maxBlue = [], []
    for _ in range(m):
        c, f, t = input().split()
        f, t = int(f), int(t)
        if c == 'B':
            heapq.heappush(maxBlue, (0, f, t))
            heapq.heappush(minBlue, (1, f, t))
        else: # R
            heapq.heappush(maxBlue, (1, f, t))
            heapq.heappush(minBlue, (0, f, t))
    minCount = kruskal(minBlue)
    maxCount = total_edge - kruskal(maxBlue)
    print(1 if minCount <= k <= maxCount else 0)
