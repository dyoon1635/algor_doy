import sys
from math import log2
from collections import deque
input = sys.stdin.readline

def init():
    dq = deque()
    dq.append((1, 0))
    visited[1] = True

    while dq:
        node, level = dq.popleft()
        for next, cost in adj[node]:
            if not visited[next]:
                visited[next] = True
                depth[next] = level + 1
                dp[next][0] = [node, cost]
                dq.append((next, level + 1))

    for j in range(1, logN):
        for i in range(1, n + 1):
            pnode = dp[dp[i][j - 1][0]][j - 1][0]
            distance = dp[i][j - 1][1] + dp[dp[i][j - 1][0]][j - 1][1]
            dp[i][j] = [pnode, distance]

def LCA(x, y):
    if depth[x] > depth[y]: x, y = y, x
    diff = depth[y] - depth[x]

    distance = 0
    for i in range(logN):
        if diff & 1 << i:
            distance += dp[y][i][1]
            y = dp[y][i][0]

    if x == y: return distance
    for i in reversed(range(logN - 1)):
        if dp[x][i][0] != dp[y][i][0]:
            distance += (dp[x][i][1] + dp[y][i][1])
            x, y = dp[x][i][0], dp[y][i][0]
    distance += (dp[x][0][1] + dp[y][0][1])
    return distance

n = int(input())
logN = int(log2(n) + 1)

parent = [i for i in range(n + 1)]
visited = [False for _ in range(n + 1)]
depth = [0 for _ in range(n + 1)]
adj = [[] for _ in range(n + 1)]
dp = [[[0, 0] for _ in range(logN)] for _ in range(n + 1)] # parent_node, distance

for _ in range(n - 1):
    a, b, w = map(int, input().split())
    adj[a].append((b, w))
    adj[b].append((a, w))

init()
for _ in range(int(input())):
    node1, node2 = map(int, input().split())
    print(LCA(node1, node2))