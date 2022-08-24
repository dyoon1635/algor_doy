import sys, math
n = int(input())
RGB = []
for _ in range(n):
    RGB.append(list(map(int, sys.stdin.readline().split())))

res = math.inf
for i in range(3):
    dp = [[math.inf] * 3 for _ in range(n)]
    dp[0][i] = RGB[0][i]
    for j in range(1, n):
        dp[j][0] = RGB[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = RGB[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = RGB[j][2] + min(dp[j - 1][0], dp[j - 1][1])
    for j in range(3):
        if i == j: continue
        res = min(res, dp[n - 1][j])
print(res)
