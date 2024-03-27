import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def out_of_bound(x, y, n, m):
    return (x < 0 or x >= n or y < 0 or y >= m)

def main():
    m, n = map(int, input().split())
    dq, fire = deque(), deque()
    visited = [[False] * m for _ in range(n)]
    board = []

    for _ in range(n):
        board.append(list(input().strip()))

    for i, row in enumerate(board):
        for j, each in enumerate(row):
            if each == '@':
                dq.append((i, j, 0)) # x, y, move
                visited[i][j] = True
                board[i][j] = '.'
            if each == '*':
                fire.append((i, j))

    while dq:
        # move fire
        for _ in range(len(fire)):
            x, y = fire.popleft()
            for dir in range(4):
                nx, ny = x + dx[dir], y + dy[dir]
                if out_of_bound(nx, ny, n, m) or board[nx][ny] != '.': continue
                board[nx][ny] = '*'
                fire.append((nx, ny))
        # move character
        for _ in range(len(dq)):
            x, y, k = dq.popleft()
            for dir in range(4):
                nx, ny = x + dx[dir], y + dy[dir]
                if out_of_bound(nx, ny, n, m): return k + 1

                if visited[nx][ny] or board[nx][ny] != '.': continue
                visited[nx][ny] = True
                dq.append((nx, ny, k + 1))
    return 'IMPOSSIBLE'

for _ in range(int(input())):
    print(main())
