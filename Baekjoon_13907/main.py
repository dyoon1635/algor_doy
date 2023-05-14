import sys, heapq
input = sys.stdin.readline

def dijkstra(s):
    pq = [(0, 0, s)] # cost, edge_num, cur_node
    dist[s][0] = 0
    while pq:
        cur_cost, edge_num, cur_node = heapq.heappop(pq)
        check = False
        for edge in range(edge_num + 1):
            if dist[cur_node][edge] < cur_cost:
                check = True
                break
        if check: continue

        for next_node, next_cost in adj[cur_node]:
            new_cost = cur_cost + next_cost
            if new_cost >= dist[next_node][edge_num + 1]: continue
            dist[next_node][edge_num + 1] = new_cost
            if edge_num + 1 == m: continue
            heapq.heappush(pq, (new_cost, edge_num + 1, next_node))

n, m, k = map(int, input().split())
s, d = map(int, input().split())
dist = [[sys.maxsize] * (m + 1) for _ in range(n + 1)]  # [node][edge's num]
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    adj[a].append((b, w))
    adj[b].append((a, w))
dijkstra(s)

ans = sys.maxsize
for edge_num in range(1, m + 1):
    if dist[d][edge_num] < ans:
        ans = dist[d][edge_num]
        used = edge_num
print(ans)
for _ in range(k):
    p = int(input())
    ans = sys.maxsize
    for edge_num in range(1, used + 1):
        dist[d][edge_num] += (p * edge_num)
        if ans > dist[d][edge_num]:
            ans = dist[d][edge_num]
            used = edge_num
    print(ans)