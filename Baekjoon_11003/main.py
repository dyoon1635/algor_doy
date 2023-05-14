from collections import deque

n, l = map(int, input().split())
arr = list(map(int, input().split()))
dq = deque()

for idx, num in enumerate(arr):
    if not dq:
        dq.append((num, idx))
        print(dq[0][0], end=' ')
        continue
    left = idx - l + 1
    if left >= 0 and dq[0][1] < left:
        dq.popleft()
    while dq and dq[-1][0] > num: dq.pop()
    dq.append((num, idx))
    print(dq[0][0], end=' ')