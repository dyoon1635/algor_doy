import sys
input = sys.stdin.readline

n, t = map(int, input().split())
arr = []
dp = [0 for _ in range(t + 1)]
total = 0
for _ in range(n):
    d, m = map(int, input().split())
    total += m
    arr.append((d, m))

for day, cost in arr:
    for i in reversed(range(day, t + 1)):
        dp[i] = max(dp[i], dp[i - day] + cost)
result = total - max(dp)
print(0 if result < 0 else result)
