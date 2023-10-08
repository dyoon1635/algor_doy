import sys
input = sys.stdin.readline

c, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0] + [sys.maxsize for _ in range(c + 100)]

for i in range(1, c + 100):
    for cost, client in arr:
        if i - client < 0: continue
        dp[i] = min(dp[i], dp[i - client] + cost)
print(min(dp[c:]))