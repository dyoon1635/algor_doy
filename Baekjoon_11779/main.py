import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
adj = [[] for _ in range(n + 1)] # s -> d : cost
for _ in range(m):
    s, d, cost = map(int, sys.stdin.readline().split())
    adj[s].append([d, cost])
start, end = map(int, sys.stdin.readline().split())

result = [[sys.maxsize, i] for i in range(n + 1)]
q = deque()
q.append([0, start]) # total_cost, start
result[start][0] = 0
while q:
    cost, cur = q.popleft()
    if cost > result[cur][0]: continue

    for next, next_cost in adj[cur]:
        path_cost = next_cost + cost
        if path_cost < result[next][0]:
            result[next] = [path_cost, cur]
            q.append([path_cost, next])

route = [end]
while True:
    if route[-1] == start: break
    route.append(result[route[-1]][1])

print(result[end][0])
print(len(route))
for each in reversed(route):
    print(each, end=' ')