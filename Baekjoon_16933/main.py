import sys
from collections import deque

input = sys.stdin.readline

def solve():
    dq = deque()
    dq.append((0, 0, 0, 1)) # x, y, k, dist
    visited[0][0] = True
    while dq:
        x, y, depth, dist = dq.popleft()
        if x == n - 1 and y == m - 1: return dist
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if not (0 <= nx < n and 0 <= ny < m): continue
            if board[nx][ny]: # if wall
                if depth >= k: continue
                if dist % 2 == 0: # if night
                    dq.append((x, y, depth, dist + 1))
                else:
                    if depth < visited[nx][ny]:
                        visited[nx][ny] = depth
                        dq.append((nx, ny, depth + 1, dist + 1))
            else: # if road
                if depth < visited[nx][ny]:
                    visited[nx][ny] = depth
                    dq.append((nx, ny, depth, dist + 1))
    return -1

n, m, k = map(int, input().split())
board = []
visited = [[sys.maxsize] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(n):
    board.append(list(map(int, list(input().strip()))))
print(solve())