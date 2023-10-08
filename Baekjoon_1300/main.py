n, k = int(input()), int(input())
start, end = 0, k

answer = 0
while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for row in range(1, n + 1):
        tmp += min(n, mid // row)
    if tmp >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)