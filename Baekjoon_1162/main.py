import sys, heapq, math
n, m, K = map(int, input().split())
city = [[] * (n + 1) for _ in range(n + 1)]
inf = math.inf
for _ in range(m):
    x, y, t = map(int, sys.stdin.readline().split())
    city[x].append([y, t])
    city[y].append([x, t])

def dijkstra(start=1, end=n):
    dist = [[inf] * (n + 1) for _ in range(K + 1)]
    dist[0][start] = 0
    pq = []
    heapq.heappush(pq, [0, start, 0]) # [distance, node, k]

    while pq:
        cur_dist, node, k = heapq.heappop(pq)
        if dist[k][node] < cur_dist: continue
        for next, cost in city[node]:
            if dist[k][next] > cur_dist + cost:
                dist[k][next] = cur_dist + cost
                heapq.heappush(pq, [cur_dist + cost, next, k])
            if k < K and dist[k + 1][next] > cur_dist:
                dist[k + 1][next] = cur_dist
                heapq.heappush(pq, [cur_dist, next, k + 1])
    res = inf
    for i in range(K + 1):
        res = min(res, dist[i][end])
    return res
print(dijkstra())