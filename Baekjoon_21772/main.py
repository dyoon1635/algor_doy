import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def out_of_bound(x, y):
    return not (0 <= x < r and 0 <= y < c)

def dfs(i, j, k, cnt):
    global result
    if k == t:
        result = max(result, cnt)
        return

    for dir in range(4):
        nx, ny = i + dx[dir], j + dy[dir]
        if out_of_bound(nx, ny) or board[nx][ny] == '#':
            continue

        if board[nx][ny] == 'S':
            board[nx][ny] = '.'
            dfs(nx, ny, k + 1, cnt + 1)
            board[nx][ny] = 'S'
        else: dfs(nx, ny, k + 1, cnt)

r, c, t = map(int, input().split())
board = []
result = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
sx, sy = -1, -1
for i in range(r):
    tmp = list(input().strip())
    board.append(tmp)
    for j, each in enumerate(tmp):
        if each == 'G': sx, sy = i, j
dfs(sx, sy, 0, 0)
print(result)
