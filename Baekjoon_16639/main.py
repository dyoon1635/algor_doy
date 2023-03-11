import sys
INF = sys.maxsize
n = int(input())
string = input()

m = n // 2 + 1
max_dp = [[-sys.maxsize] * m for _ in range(m)]
min_dp = [[sys.maxsize] * m for _ in range(m)]
for i in range(m):
    max_dp[i][i] = int(string[i * 2])
    min_dp[i][i] = int(string[i * 2])

for k in range(1, m):
    for i in range(m - k):
        j = i + k
        for x in range(i, j):
            max_dp[i][j] = max(max_dp[i][j], eval(str(max_dp[i][x]) + string[x * 2 + 1] + str(max_dp[x + 1][j])))
            max_dp[i][j] = max(max_dp[i][j], eval(str(max_dp[i][x]) + string[x * 2 + 1] + str(min_dp[x + 1][j])))
            max_dp[i][j] = max(max_dp[i][j], eval(str(min_dp[i][x]) + string[x * 2 + 1] + str(max_dp[x + 1][j])))
            max_dp[i][j] = max(max_dp[i][j], eval(str(min_dp[i][x]) + string[x * 2 + 1] + str(min_dp[x + 1][j])))

            min_dp[i][j] = min(min_dp[i][j], eval(str(max_dp[i][x]) + string[x * 2 + 1] + str(max_dp[x + 1][j])))
            min_dp[i][j] = min(min_dp[i][j], eval(str(max_dp[i][x]) + string[x * 2 + 1] + str(min_dp[x + 1][j])))
            min_dp[i][j] = min(min_dp[i][j], eval(str(min_dp[i][x]) + string[x * 2 + 1] + str(max_dp[x + 1][j])))
            min_dp[i][j] = min(min_dp[i][j], eval(str(min_dp[i][x]) + string[x * 2 + 1] + str(min_dp[x + 1][j])))
print(max_dp[0][-1])