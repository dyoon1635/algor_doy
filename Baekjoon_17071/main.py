from collections import deque
MAX = 500_000

n, k = map(int, input().split())
visited = [[-1] * (MAX + 1) for _ in range(2)] # 0 : 짝수, 1 : 홀수

q = deque()
q.append(n)
visited[0][n] = 0
t = 0
while q:
    t += 1
    for _ in range(len(q)):
        cur = q.popleft()
        for next in [cur + 1, cur - 1, cur * 2]:
            if next > MAX or next < 0 or visited[t % 2][next] != -1: continue
            visited[t % 2][next] = t
            q.append(next)

t = 0
while k <= MAX:
    if visited[t % 2][k] != -1 and visited[t % 2][k] <= t:
        print(t)
        exit(0)
    t += 1
    k += t
print(-1)
