n = int(input())
arr1 = list(map(int, input().split()))
arr2 = arr1[::-1]

n, m = len(arr1), len(arr2)
arr1 = ['0'] + arr1
arr2 = ['0'] + arr2

dp = [[0] * (m + 1) for _ in range(n + 1)]
res = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if arr1[i] == arr2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        res = max(res, dp[i][j])
print(n - res)