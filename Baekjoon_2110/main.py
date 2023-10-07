import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = list(sorted(int(input()) for _ in range(n)))
start, end = 1, arr[-1] - arr[0]

answer = 0
while start <= end:
    mid = (start + end) // 2
    count = 1
    node = arr[0]

    for each in arr:
        if each >= node + mid:
            count += 1
            node = each
    if count >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)