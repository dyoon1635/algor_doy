str1 = ['0'] + list(input().strip())
str2 = ['0'] + list(input().strip())

n, m = len(str1) - 1, len(str2) - 1
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
ans = 0
for each in dp:
    ans = max(ans, max(each))
print(ans)