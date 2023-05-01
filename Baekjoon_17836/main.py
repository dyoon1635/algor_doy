import sys
from collections import deque
input = sys.stdin.readline

def out_of_bound(x, y):
    return not (0 <= x < n and 0 <= y < m)

def bfs():
    visited[0][0][0] = True
    dq.append((0, 0, 0, 0)) # GRAM, x, y, t
    while dq:
        GRAM, x, y, cur_t = dq.popleft()
        if x == n - 1 and y == m - 1:
            return cur_t
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if not out_of_bound(nx, ny) and cur_t + 1 <= t and not visited[GRAM][nx][ny]:
                if board[nx][ny] == 1:
                    if GRAM:
                        visited[GRAM][nx][ny] = True
                        dq.append((GRAM, nx, ny, cur_t + 1))
                else:
                    if board[nx][ny] == 2:
                        visited[1][nx][ny] = True
                        dq.append((1, nx, ny, cur_t + 1))
                    else: # board[nx][ny] == 0
                        visited[GRAM][nx][ny] = True
                        dq.append((GRAM, nx, ny, cur_t + 1))
    return 'Fail'

n, m, t = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[[False] * m for _ in range(n)] for _ in range(2)]
board = [list(map(int, input().split())) for _ in range(n)]
dq = deque()
print(bfs())