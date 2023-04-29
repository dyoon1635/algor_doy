n = int(input())
num2set = [2 ** k for k in range(21)]
MOD = 10 ** 9
dp = [1] + [0 for _ in range(n)]
for each in num2set:
    if each <= n:
        for i in range(each, n + 1):
            dp[i] += (dp[i - each]) % MOD
print(dp[n] % MOD)