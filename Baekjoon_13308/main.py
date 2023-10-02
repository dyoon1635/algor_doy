import sys, heapq
input = sys.stdin.readline

def solve():
    distance = [[sys.maxsize] * (max(cost) + 1) for _ in range(n + 1)]
    pq = []
    distance[1][cost[1]] = 0
    heapq.heappush(pq, (0, cost[1], 1))
    while pq:
        dist, cur_cost, node = heapq.heappop(pq)
        if node == n: return dist
        if distance[node][cur_cost] < dist: continue

        for next_node, next_dist in adj[node]:
            next_cost = min(cost[next_node], cur_cost)

            if distance[next_node][cur_cost] > dist + next_dist * cur_cost:
                distance[next_node][cur_cost] = dist + next_dist * cur_cost
                heapq.heappush(pq, (dist + next_dist * cur_cost, next_cost, next_node))

n, m = map(int, input().split())
cost = [-1] + list(map(int, input().split()))
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    adj[a].append((b, w))
    adj[b].append((a, w))
print(solve())