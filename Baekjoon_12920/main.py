n, m = map(int, input().split())

dp = [0 for _ in range(m + 1)]
q = []
for _ in range(n):
    w, c, k = map(int, input().split())

    i = 1
    while k > 0:
        tmp = min(i, k)
        q.append((w * tmp, c * tmp))
        k -= i; i *= 2

for weight, value in q:
    for i in range(m, weight - 1, -1):
        dp[i] = max(dp[i], dp[i - weight] + value)
print(dp[-1])