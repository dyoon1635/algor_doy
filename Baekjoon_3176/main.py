import sys, math
from collections import deque
input = sys.stdin.readline

n = int(input())
logN = int(math.log2(n) + 1)
depth = [0 for _ in range(n + 1)]
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

parent = [[0, 0] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
dq = deque([1])
visited[1] = True

while dq:
    node = dq.popleft()
    for next, cost in tree[node]:
        if not visited[next]:
            visited[next] = True
            dq.append(next)
            depth[next] = depth[node] + 1
            parent[next][0] = node
            parent[next][1] = cost

# 2^x, shortest, longest
dp = [[[0, 0, 0] for _ in range(logN)] for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0][0] = parent[i][0]
    dp[i][0][1] = parent[i][1]
    dp[i][0][2] = parent[i][1]

# sparse matrix
for j in range(1, logN):
    for i in range(1, n + 1):
        dp[i][j][0] = dp[dp[i][j - 1][0]][j - 1][0]
        dp[i][j][1] = min(dp[dp[i][j - 1][0]][j - 1][1], dp[i][j - 1][1])
        dp[i][j][2] = max(dp[dp[i][j - 1][0]][j - 1][2], dp[i][j - 1][2])

k = int(input())
for _ in range(k):
    d, e = map(int, input().split())
    if depth[d] < depth[e]:
        d, e = e, d

    shortest, longest = sys.maxsize, 0
    for i in range(logN):
        if (depth[d] - depth[e]) & (1 << i):
            shortest = min(shortest, dp[d][i][1])
            longest = max(longest, dp[d][i][2])
            d = dp[d][i][0]

    if d == e:
        print(shortest, longest)
        continue

    for i in range(logN - 1, -1, -1):
        if dp[d][i][0] != dp[e][i][0]:
            shortest = min(shortest, dp[d][i][1], dp[e][i][1])
            longest = max(longest, dp[d][i][2], dp[e][i][2])
            d, e = dp[d][i][0], dp[e][i][0]
    shortest = min(shortest, dp[d][i][1], dp[e][i][1])
    longest = max(longest, dp[d][i][2], dp[e][i][2])
    print(shortest, longest)
