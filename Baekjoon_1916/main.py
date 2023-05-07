import sys, heapq
input = sys.stdin.readline

def dijkstra(node):
    pq = []
    heapq.heappush(pq, (node, 0))
    dist = [sys.maxsize for _ in range(n + 1)]
    dist[node] = 0

    while pq:
        cur_node, cur_cost = heapq.heappop(pq)
        if dist[cur_node] < cur_cost: continue
        for next_node, next_cost in adj[cur_node]:
            new_cost = cur_cost + next_cost
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(pq, (next_node, new_cost))
    return dist[end]

n = int(input())
m = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
start, end = map(int, input().split())
print(dijkstra(start))