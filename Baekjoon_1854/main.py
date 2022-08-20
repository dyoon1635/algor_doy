import sys, math, heapq
n, m, k = map(int, input().split())
city = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    city[a].append([b, c])

def dijkstra(start):
    dist = [[math.inf] * k for _ in range(n + 1)]
    heapq.heappush(dist[start], 0)

    q = []
    heapq.heappush(q, [0, start])
    while q:
        d, cur = heapq.heappop(q)
        for nx, nd in city[cur]:
            if dist[nx][k - 1] > nd + d:
                heapq.heappush(q, [nd + d, nx])
                dist[nx][k - 1] = nd + d
                dist[nx].sort()
    return dist

result = dijkstra(1)
for i in range(1, n + 1):
    if result[i][k - 1] == math.inf: print(-1)
    else: print(result[i][k - 1])
    #print(result[i])
