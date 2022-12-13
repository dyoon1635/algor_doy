import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
board = []
for _ in range(r):
    board.append(list(sys.stdin.readline().strip()))

visited = [[False] * c for _ in range(r)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
next_q = deque()

swan_pos = []
swan_idx = []
for i, row in enumerate(board):
    for j, each in enumerate(row):
        if each == 'L':
            swan_pos.append([i, j])
            swan_idx.append(c * i + j)
            board[i][j] = '.'

parent = [i for i in range(r * c)]

def find(x):
    if x != parent[x]: parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a, b = find(x), find(y)
    if a < b: parent[b] = a
    else: parent[a] = b

def get_idx(x, y):
    return c * x + y

def out_of_bound(x, y):
    return (x < 0 or x >= r or y < 0 or y >= c)

def bfs(x, y):
    q = deque()
    q.append([x, y])
    while q:
        cx, cy = q.popleft()
        c_idx = get_idx(cx, cy)
        for dir in range(4):
            nx, ny = cx + dx[dir], cy + dy[dir]
            if out_of_bound(nx, ny) or visited[nx][ny]: continue
            visited[nx][ny] = True
            n_idx = get_idx(nx, ny)
            if board[nx][ny] == '.':
                union(c_idx, n_idx)
                q.append([nx, ny])
            elif board[nx][ny] == 'X':
                next_q.append([nx, ny, c_idx])

def melt():
    global board, visited
    q = next_q.copy()
    next_q.clear()

    while q:
        cx, cy, ex_idx = q.popleft()
        visited[cx][cy] = True
        board[cx][cy] = '.'
        c_idx = get_idx(cx, cy)
        union(c_idx, ex_idx)
        for dir in range(4):
            nx, ny = cx + dx[dir], cy + dy[dir]
            if out_of_bound(nx, ny): continue

            n_idx = get_idx(nx, ny)
            if board[nx][ny] == '.':
                union(c_idx, n_idx)
            if board[nx][ny] == 'X' and not visited[nx][ny]:
                visited[nx][ny] = True
                next_q.append([nx, ny, c_idx])

for i in range(r):
    for j in range(c):
        if board[i][j] == '.' and not visited[i][j]:
            visited[i][j] = True
            bfs(i, j)

day = 0
while find(swan_idx[0]) != find(swan_idx[1]):
    melt()
    day += 1
print(day)