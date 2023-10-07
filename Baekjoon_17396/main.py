import sys, heapq
input = sys.stdin.readline

def dikjstra():
    distance = [0] + [sys.maxsize for _ in range(n - 1)]
    pq = [(0, 0)] # cur_cost, cur_node
    while pq:
        cost, node = heapq.heappop(pq)
        if distance[node] < cost: continue
        for next_node, next_cost in adj[node]:
            if visible[next_node]: continue
            new_cost = cost + next_cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))
    print(-1 if distance[-1] == sys.maxsize else distance[-1])

n, m = map(int, input().split())
visible = list(map(int, input().split()))[:-1] + [0]
adj = [[] for _ in range(n)]

for _ in range(m):
    a, b, t = map(int, input().split())
    adj[a].append((b, t))
    adj[b].append((a, t))
dikjstra()
