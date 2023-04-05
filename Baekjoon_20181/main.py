n, k = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0 for _ in range(n)]

cur_max, cur_total = 0, 0
lp, rp = 0, 0
while True:
    if cur_total >= k:
        cur_max = 0 if lp == 0 else max(cur_max, dp[lp - 1])
        dp[rp - 1] = max(dp[rp - 1], cur_max + cur_total - k)
        cur_total -= arr[lp]
        lp += 1
    elif rp == n: break
    else:
        cur_total += arr[rp]
        rp += 1
print(max(dp))