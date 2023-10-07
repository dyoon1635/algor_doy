import sys, heapq
input = sys.stdin.readline

def dijkstra():
    distance = [sys.maxsize for _ in range(n + 1)]
    distance[1] = 0
    pq = [(0, 1)] # cost, node

    while pq:
        cost, node = heapq.heappop(pq)
        if cost > distance[node]: continue
        for next_node, next_cost in adj[node]:
            new_cost = cost + next_cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))
    print(distance[-1])

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))
dijkstra()