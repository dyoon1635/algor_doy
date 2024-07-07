MOD = 10 ** 9 + 7
dp = [[0] * 101 for _ in range(101)]
dp[0][0] = 1

n, m, p = map(int, input().split())
for i in range(1, p + 1):
    for j in range(n + 1):
        if j > 0:
            dp[i][j] = (dp[i][j] + (dp[i - 1][j - 1] * (n - j + 1)) % MOD) % MOD
        if j > m:
            dp[i][j] = (dp[i][j] + (dp[i - 1][j] * (j - m)) % MOD) % MOD
print(dp[p][n])