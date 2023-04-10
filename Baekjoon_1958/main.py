str1 = ['0'] + list(input().strip())
str2 = ['0'] + list(input().strip())
str3 = ['0'] + list(input().strip())
n, m, l = len(str1) - 1, len(str2) - 1, len(str3) - 1
dp = [[[0] * (l + 1) for _ in range(m + 1)] for _ in range(n + 1)]

result = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        for k in range(1, l + 1):
            if str1[i] == str2[j] and str1[i] == str3[k]:
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
            else:
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
            result = max(result, dp[i][j][k])
print(result)