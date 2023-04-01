str1, str2 = ['0'] + list(input()), ['0'] + list(input())
n, m = len(str1), len(str2)
dp = [[""] * m for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i - 1][j - 1] + str2[j]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]
print(len(dp[-1][-1]))
print(dp[-1][-1])