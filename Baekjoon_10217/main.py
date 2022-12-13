import sys
from collections import deque

T = int(input())
for _ in range(T):
    n, m, k = map(int, sys.stdin.readline().split())
    dp = [[sys.maxsize] * (n + 1) for _ in range(m + 1)]
    adj = [[] for _ in range(n + 1)]
    for _ in range(k):
        u, v, c, d = map(int, sys.stdin.readline().split())
        adj[u].append([v, c, d])
    q = deque()
    q.append([1, 0, 0])
    while q:
        node, cost, distance = q.popleft()
        if dp[cost][node] < distance: continue

        for next_node, add_cost, add_distance in adj[node]:
            new_cost = cost + add_cost
            new_distance = distance + add_distance
            if new_cost > m or new_distance >= dp[new_cost][next_node]: continue
            for c in range(new_cost, m + 1):
                if dp[c][next_node] > new_distance: dp[c][next_node] = new_distance
                else: break
            q.append([next_node, new_cost, dp[new_cost][next_node]])
    print(dp[m][n] if dp[m][n] != sys.maxsize else 'Poor KCM')
