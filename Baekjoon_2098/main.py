import sys
n = int(input())
inf = sys.maxsize
dp = [[-1] * (1 << n) for _ in range(n)]
w = []
for _ in range(n):
    w.append(list(map(int, sys.stdin.readline().split())))

def dfs(cur, visited):
    if visited == (1 << n) - 1:
        if w[cur][0]: return w[cur][0]
        else: return inf

    if dp[cur][visited] != -1: return dp[cur][visited]
    dp[cur][visited] = inf
    for i in range(1, n):
        if not w[cur][i] or visited & (1 << i): continue
        dp[cur][visited] = min(dp[cur][visited],
                               dfs(i, visited | (1 << i)) + w[cur][i])
    return dp[cur][visited]
print(dfs(0, 1))