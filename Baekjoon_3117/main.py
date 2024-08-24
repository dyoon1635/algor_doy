import sys
input = sys.stdin.readline

n, k, m = map(int, input().split())
student = [*map(int, input().split())]
dp = [[0] + [*map(int, input().split())]] + \
     [[0] * (k + 1) for _ in range(30)]

for step in range(1, 31):
    for video in range(1, k + 1):
        dp[step][video] = dp[step - 1][dp[step - 1][video]]

for i in range(31):
    if (1 << i) & (m - 1):
        for each in range(n):
            student[each] = dp[i][student[each]]
print(*student)