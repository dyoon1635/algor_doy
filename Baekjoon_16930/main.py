from collections import deque

n, m, k = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = [[-1] * m for _ in range(n)]
result[x1 - 1][y1 - 1] = 0
dq = deque([(x1 - 1, y1 - 1)])

while dq:
    x, y = dq.popleft()
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        nk = 1
        while nk <= k and 0 <= nx < n and 0 <= ny < m and board[nx][ny] != '#':
            if result[nx][ny] != -1 and result[nx][ny] <= result[x][y]: break
            if result[nx][ny] == -1:
                dq.append((nx, ny))
                result[nx][ny] = result[x][y] + 1
            nx, ny, nk = nx + dx[dir], ny + dy[dir], nk + 1
print(result[x2 - 1][y2 - 1])
