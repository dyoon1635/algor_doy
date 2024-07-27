import sys
from collections import deque
input = sys.stdin.readline
MAX = 100_001

dq = deque()
n, k = map(int, input().split())
dq.append(n)
count = [0 for _ in range(MAX)]
cnt, result = 0, 0

while dq:
    node = dq.popleft()
    tmp = count[node]

    if node == k:
        result = tmp
        cnt += 1
        continue

    for idx in [node - 1, node + 1, node * 2]:
        if 0 <= idx < MAX and (count[idx] == 0 or count[idx] == count[node] + 1):
            count[idx] = count[node] + 1
            dq.append(idx)

print(result)
print(cnt)
