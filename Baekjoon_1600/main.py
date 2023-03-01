import sys
from collections import deque
input = sys.stdin.readline

def out_of_bound(x, y):
    return not (0 <= x < n and 0 <= y < m)

def bfs():
    dq = deque()
    dq.append((0, 0, 0, 0)) # 시작점, 이동 횟수, k-count

    while dq:
        cx, cy, d, k = dq.popleft()
        if cx == n - 1 and cy == m - 1:
            return d

        for dir in range(4):
            nx, ny = cx + dx[dir], cy + dy[dir]
            if out_of_bound(nx, ny) \
                or visited[k][nx][ny] \
                or board[nx][ny]: continue
            visited[k][nx][ny] = True
            dq.append((nx, ny, d + 1, k))

        if k < K:
            for dir in range(8):
                nx = cx + knight_dx[dir]
                ny = cy + knight_dy[dir]
                if out_of_bound(nx, ny) \
                        or visited[k + 1][nx][ny] \
                        or board[nx][ny]: continue
                visited[k + 1][nx][ny] = True
                dq.append((nx, ny, d + 1, k + 1))
    return -1

dx = [-1, 0, 1 , 0]
dy = [0, 1, 0, -1]
knight_dx = [-2, -1, 1, 2, 2, 1, -1, -2]
knight_dy = [1, 2, 2, 1, -1, -2, -2, -1]

K = int(input())
m, n = map(int, input().split())
board = []
visited = [[[False] * m for _ in range(n)] for _ in range(K + 1)]
for _ in range(n):
    board.append(list(map(int, input().split())))
print(bfs())
