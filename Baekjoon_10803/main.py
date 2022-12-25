n, m = map(int, input().split())

if n > m: n, m = m, n

dp = [[n * m] * (m + 1) for _ in range(n + 1)]
dp[1] = [i for i in range(m + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == j: dp[i][j] = 1
        elif i > j:
            dp[i][j] = dp[j][i]
        elif i * 3 <= j:
            dp[i][j] = min(dp[i][j], dp[i][j - i] + 1)
        else:
            for k in range(1, i // 2 + 1):
                dp[i][j] = min(dp[i][j],
                               dp[k][j] + dp[i - k][j])
            for k in range(1, j // 2 + 1):
                dp[i][j] = min(dp[i][j],
                               dp[i][k] + dp[i][j - k])
print(dp[n][m])