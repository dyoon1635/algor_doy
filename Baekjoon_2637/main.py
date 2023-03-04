import sys
from collections import deque
input = sys.stdin.readline

n, m = int(input()), int(input())
adj = [[] for _ in range(n + 1)]
re_adj = [[] for _ in range(n + 1)]
in_degree = [0 for _ in range(n + 1)]
for _ in range(m):
    x, y, k = map(int, input().split())
    # x를 만들기 위해 y가 k개 필요함
    adj[y].append([x, k])
    re_adj[x].append([y, k])
    in_degree[x] += 1

parts = deque()
basic_parts = []
for each_part in range(1, n + 1):
    if not in_degree[each_part]:
        parts.append(each_part)
        basic_parts.append(each_part)

topology = []
while parts:
    tmp = parts.popleft()
    topology.append(tmp)

    for next, _ in adj[tmp]:
        in_degree[next] -= 1
        if not in_degree[next]: parts.append(next)

dp = [0 for _ in range(n)] + [1]
for each in reversed(range(n)):
    cur = topology[each]
    for next, cost in re_adj[cur]:
        dp[next] += cost * dp[cur]

for each_part in basic_parts:
    print(each_part, dp[each_part])