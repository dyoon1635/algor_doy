import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def out_of_bound(x, y):
    return not (0 <= x < n and 0 <= y < n)

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[max(x, y)] = min(x, y)

def merge(a, b):
    global connected
    pa, pb = find(a), find(b)
    if pa != pb:
        union(pa, pb)
        connected += 1

def bfs():
    for _ in range(len(dq)):
        x, y, civil = dq.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if out_of_bound(nx, ny):
                continue
            if board[nx][ny]:
                merge(civil, board[nx][ny])
                continue
            board[nx][ny] = civil
            dq.append((nx, ny, civil))
            for next_dir in range(4):
                nnx, nny = nx + dx[dir], ny + dy[dir]
                if not out_of_bound(nnx, nny) and board[nnx][nny]:
                    merge(civil, board[nnx][nny])


n, k = map(int, input().split())
parent = [i for i in range(k + 1)]
board = [[0] * n for _ in range(n)]
dq = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(1, k + 1):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    board[x][y] = i
    dq.append((x, y, i))

connected = 0
for x, y, civil in dq:
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if out_of_bound(nx, ny):
            continue
        if board[nx][ny]:
            merge(civil, board[nx][ny])

year = 0
while connected != k - 1:
    year += 1
    bfs()
print(year)
