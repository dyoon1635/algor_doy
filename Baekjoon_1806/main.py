n, s = map(int, input().split())
arr = list(map(int, input().split()))

lp, rp, cur_sum = 0, 0, arr[0]
ans = n + 1
while lp <= rp:
    if cur_sum < s:
        rp += 1
        if rp == n: break
        cur_sum += arr[rp]
    else:
        cur_sum -= arr[lp]
        ans = min(ans, rp - lp + 1)
        lp += 1
print(ans if ans != n + 1 else 0)