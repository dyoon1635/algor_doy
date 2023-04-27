import sys
from collections import deque
input = sys.stdin.readline

def out_of_bound(x, y):
    return not (0 <= x < n and 0 <= y < n)

def bfs():
    for _ in range(s):
        for each_virus in range(1, k + 1):
            for _ in range(len(virus[each_virus])):
                x, y = virus[each_virus].popleft()
                for dir in range(4):
                    nx, ny = x + dx[dir], y + dy[dir]
                    if not out_of_bound(nx, ny) and not board[nx][ny]:
                        board[nx][ny] = each_virus
                        virus[each_virus].append((nx, ny))

n, k = map(int, input().split())
board = []
virus = [deque() for _ in range(k + 1)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j]:
            virus[tmp[j]].append((i, j))
    board.append(tmp)
s, x, y = map(int, input().split())
bfs()
print(board[x - 1][y - 1])