from collections import deque
import sys

n, m = map(int, input().split())
s, e = map(int, input().split())
connect = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    connect[x].append(y)
    connect[y].append(x)

def solve():
    dq = deque() # location, move
    dq.append([s, 0])
    while dq:
        loc, move = dq.popleft()

        if loc + 1 <= n and not visited[loc + 1]:
            if loc + 1 == e: return move + 1
            visited[loc + 1] = True
            dq.append([loc + 1, move + 1])

        if loc - 1 > 0 and not visited[loc - 1]:
            if loc - 1 == e: return move + 1
            visited[loc - 1] = True
            dq.append([loc - 1, move + 1])

        for i in connect[loc]:
            if not visited[i]:
                if i == e: return move + 1
                visited[i] = True
                dq.append([i, move + 1])
print(solve())