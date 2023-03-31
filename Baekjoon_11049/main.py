import sys
input = sys.stdin.readline

n = int(input())
matrix = []
for _ in range(n):
    r, c = map(int, input().split())
    matrix.append((r, c))

dp = [[sys.maxsize] * n for _ in range(n)]
for i in range(n - 1):
    dp[i][i + 1] = matrix[i][0] * matrix[i][1] * matrix[i + 1][1]
for i in range(n):
    dp[i][i] = 0

for i in reversed(range(n - 2)):
    for j in range(i + 1, n):
        for k in range(i, j):
            #print(i, k, j)
            #print(dp[i][k], dp[k + 1][j])
            #print(matrix[i][0], matrix[k][1], matrix[j][1])
            dp[i][j] = min(dp[i][j],
                           dp[i][k] + dp[k + 1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])
print(dp[0][-1])
