import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    adj[a].append([b, c])
    adj[b].append([a, c])

dist = [[sys.maxsize, i] for i in range(n + 1)] # cost, parent
q = deque()
q.append([0, 1])

while q:
    cost, cur = q.popleft()
    if dist[cur][0] < cost: continue

    for next, next_cost in adj[cur]:
        if cost + next_cost < dist[next][0]:
            dist[next] = [cost + next_cost, cur]
            q.append([cost + next_cost, next])
print(n - 1)
for i in range(2, n + 1):
    print(i, dist[i][1])
