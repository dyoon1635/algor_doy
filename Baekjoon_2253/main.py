import sys
input = sys.stdin.readline

n, m = map(int, input().split())
impossible = [False for _ in range(n + 1)]
dp = [[sys.maxsize] * (int((2 * n) ** 0.5) + 2) for _ in range(n + 1)]
for _ in range(m):
    impossible[int(input())] = True

dp[1][0] = 0 # rock, speed
for rock in range(2, n + 1):
    if impossible[rock]: continue
    for jump in range(1, int((rock * 2) ** 0.5) + 1):
        dp[rock][jump] = min(dp[rock - jump][jump - 1],
                             dp[rock - jump][jump],
                             dp[rock - jump][jump + 1]) + 1
print(-1 if min(dp[n]) == sys.maxsize else min(dp[n]))