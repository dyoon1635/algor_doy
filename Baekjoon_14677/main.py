from collections import deque

def next(x):
    if x == 'B': return 'L'
    elif x == 'L': return 'D'
    return 'B'

n = int(input()) * 3
pills = list(input().strip())
visited = [[False] * (n + 1) for _ in range(n + 1)]

dq = deque()
dq.append((0, n - 1, 'B', 0)) # lp, rp, time, count
result = 0

while dq:
    lp, rp, t, cnt = dq.popleft()
    result = max(result, cnt)
    if lp > rp: continue
    visited[lp][rp] = True

    next_t = next(t)
    if pills[lp] == t and not visited[lp + 1][rp]:
        dq.append((lp + 1, rp, next_t, cnt + 1))
        visited[lp + 1][rp] = True
    if pills[rp] == t and not visited[lp][rp - 1]:
        dq.append((lp, rp - 1, next_t, cnt + 1))
        visited[lp][rp - 1] = True
print(result)