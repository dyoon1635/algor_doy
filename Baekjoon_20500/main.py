n = int(input())
MOD = 10 ** 9 + 7
dp = [[0] * 3 for _ in range(1516)] # dp[1][2] len = 1, mod = 2
dp[2][0] = 1; dp[2][1] = 1

for i in range(3, n + 1):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % MOD;
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD;
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % MOD;
print(dp[n][0])