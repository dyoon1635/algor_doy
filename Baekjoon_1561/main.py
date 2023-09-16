n, m = map(int, input().split())
arr = list(map(int, input().split()))

if n < m: print(n)
else:
    left, right = 0, 60_000_000_000
    t = None
    while left <= right:
        mid = (left + right) // 2
        tmp = m

        for each in arr:
            tmp += (mid // each)
        if tmp >= n:
            t = mid
            right = mid - 1
        else:
            left = mid + 1

    tmp = m
    for each in arr:
        tmp += ((t - 1) // each)
    for idx, each in enumerate(arr):
        if t % each == 0: tmp += 1
        if tmp == n:
            print(idx + 1)
            break