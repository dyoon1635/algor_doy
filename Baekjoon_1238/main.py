import sys, math, heapq

n, m, x = map(int, input().split())
inf = math.inf
adj = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    s, e, t = map(int, sys.stdin.readline().split())
    adj[s].append([e, t])

def dijkstra(s, e):
    dist = [inf] * (n + 1)
    dist[s] = 0

    q = []
    heapq.heappush(q, [0, s])
    while q:
        d, cur = heapq.heappop(q)
        for nx, nd in adj[cur]:
            if nx != cur and dist[nx] > nd + d:
                dist[nx] = nd + d
                heapq.heappush(q, [nd + d, nx])
    return dist[e]

res = 0
for i in range(1, n + 1):
    res = max(res, dijkstra(i, x) + dijkstra(x, i))
print(res)
