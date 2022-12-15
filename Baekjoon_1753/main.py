import sys, heapq

V, E = map(int, sys.stdin.readline().split())
s = int(sys.stdin.readline())
adj = [[] for _ in range(V + 1)]
distance = [sys.maxsize for _ in range(V + 1)]; distance[s] = 0
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    adj[u].append([v, w])

q = [[0, s]]
while q:
    cur_cost, cur_node = heapq.heappop(q)
    if distance[cur_node] < cur_cost: continue
    for next_node, next_cost in adj[cur_node]:
        new_cost = cur_cost + next_cost
        if new_cost >= distance[next_node]: continue
        distance[next_node] = new_cost
        heapq.heappush(q, [new_cost, next_node])
for each in distance[1:]:
    print('INF' if each == sys.maxsize else each)