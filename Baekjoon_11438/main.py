import sys
from collections import deque
from math import log2
input = sys.stdin.readline

def init():
    dq = deque()
    dq.append((1, 0))
    visited[1] = True
    while dq:
        cur_node, cur_depth = dq.popleft()
        for next in adj[cur_node]:
            if not visited[next]:
                visited[next] = True
                parent[next] = cur_node
                depth[next] = cur_depth + 1
                dq.append((next, cur_depth + 1))

n = int(input())
logN = int(log2(n) + 1)
visited = [False for _ in range(n + 1)]
parent = [i for i in range(n + 1)]
depth = [0 for _ in range(n + 1)]
adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

init()
dp = [[0] * logN for _ in range(n + 1)]
for node in range(1, n + 1):
    dp[node][0] = parent[node]

for j in range(1, logN):
    for i in range(1, n + 1):
        dp[i][j] = dp[dp[i][j - 1]][j - 1]

for _ in range(int(input())):
    node1, node2 = map(int, input().split())
    if depth[node1] > depth[node2]: node1, node2 = node2, node1

    diff = depth[node2] - depth[node1]
    for i in range(logN):
        if diff & 1 << i:
            node2 = dp[node2][i]

    if node1 == node2:
        print(node1)
        continue

    for i in range(logN -1, -1, -1):
        if dp[node1][i] != dp[node2][i]:
            node1, node2 = dp[node1][i], dp[node2][i]
    print(dp[node2][0])