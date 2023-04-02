import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memories = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))
dp = [[0] * (sum(costs) + 1) for _ in range(n + 1)]

result = sum(costs)
for i in range(1, n + 1):
    memory, cost = memories[i], costs[i]
    for j in range(1, sum(costs) + 1):
        if j < cost: dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + memory)

        if dp[i][j] >= m: result = min(result, j)
print(result if m != 0 else 0)