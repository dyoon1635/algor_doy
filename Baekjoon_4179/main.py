from collections import deque

def out_of_bound(x, y):
    return not (0 <= x < n and 0 <= y < m)

def bfs():
    dq = deque()
    dq.append((Jx, Jy, 0))
    while dq:
        for _ in range(len(dq)):
            cx, cy, t = dq.popleft()
            if board[cx][cy] == 'F': continue
            for dir in range(4):
                nx, ny = cx + dx[dir], cy + dy[dir]
                if out_of_bound(nx, ny): return t + 1
                if not visited[nx][ny] and board[nx][ny] == '.':
                    visited[nx][ny] = True
                    dq.append((nx, ny, t + 1))
        # fire
        for _ in range(len(fire)):
            fx, fy = fire.popleft()
            for dir in range(4):
                nx, ny = fx + dx[dir], fy + dy[dir]
                if not out_of_bound(nx, ny) and board[nx][ny] == '.':
                    board[nx][ny] = 'F'
                    fire.append((nx, ny))
    return 'IMPOSSIBLE'

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
board = []
Jx, Jy, fire = 0, 0, deque()
for i in range(n):
    tmp = list(input().strip())
    for j in range(m):
        if tmp[j] == 'J': Jx, Jy = i, j
        if tmp[j] == 'F': fire.append((i, j))
    board.append(tmp)
board[Jx][Jy] = '.'
print(bfs())