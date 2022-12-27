n, l, r = map(int, input().split())
dp = [[[0 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
dp[1][1][1] = 1
mod = 10 ** 9 + 7
for i in range(2, n + 1):
    for j in range(1, l + 1):
        for k in range(1, r + 1):
            dp[i][j][k] = (dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] + dp[i - 1][j][k] * (i - 2)) % mod
print(dp[n][l][r])