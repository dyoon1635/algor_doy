import sys, heapq
input = sys.stdin.readline
inf = sys.maxsize

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
path = [i for i in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

def dijskstra(x, y):
    pq = [(0, 1)] # cost, node
    distance = [inf for _ in range(n + 1)]
    distance[1] = 0

    while pq:
        cost, node = heapq.heappop(pq)
        for next_node, next_cost in adj[node]:
            if node == x and next_node == y: continue
            new_cost = cost + next_cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                path[next_node] = node
                heapq.heappush(pq, (new_cost, next_node))
    return distance[n]

answer = dijskstra(0, 0)
cur_node, pre_node = n, path[n]
while True:
    if cur_node == pre_node: break
    answer = max(answer, dijskstra(pre_node, cur_node))
    cur_node, pre_node = pre_node, path[pre_node]
print(answer)
