import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(node):
    for next in adj[node]:
        if not visited[next - 1]:
            visited[next - 1] = True
            dfs(next)
            dp[node - 1][0] += dp[next - 1][1]
            dp[node - 1][1] += min(dp[next - 1])

n = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

dp = [[0, 1] for _ in range(n)]
visited = [False for _ in range(n)]

visited[0] = True
dfs(1)
print(min(dp[0]))
