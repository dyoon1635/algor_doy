import sys
from collections import deque
input = sys.stdin.readline

def out_of_bound(x, y):
    return not (0 <= x < n and 0 <= y < m)

def bfs(i, j):
    count = 0
    visited = [[False] * m for _ in range(n)]
    visited[i][j] = True

    dq = deque()
    dq.append((i, j, 0))
    while dq:
        cx, cy, dist = dq.popleft()
        count = max(count, dist)
        for dir in range(4):
            nx, ny = cx + dx[dir], cy + dy[dir]
            if out_of_bound(nx, ny) or visited[nx][ny] or board[nx][ny] == 'W':
                continue
            visited[nx][ny] = True
            dq.append((nx, ny, dist + 1))
    return count

n, m = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = []
for _ in range(n):
    board.append(list(input().strip()))

result = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'L':
            result = max(result, bfs(i, j))
print(result)
