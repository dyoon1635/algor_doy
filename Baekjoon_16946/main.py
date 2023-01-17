import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find(x):
    if x == parent[x]: return parent[x]
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a, b = find(x), find(y)
    if x < y: parent[b] = a
    else: parent[a] = b

def out_of_bound(x, y):
    return not (0 <= x < n and 0 <= y < m)

def get_idx(x, y):
    return x * m + y

def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    visited[x][y] = True
    count = 0
    while dq:
        cx, cy = dq.popleft()
        idx = get_idx(cx, cy)
        count += 1
        for dir in range(4):
            nx, ny = cx + dx[dir], cy + dy[dir]
            if out_of_bound(nx, ny) or board[nx][ny] or visited[nx][ny]: continue
            next_idx = get_idx(nx, ny)
            visited[nx][ny] = True
            union(idx, next_idx)
            dq.append((nx, ny))
    return count

def solve():
    for i in range(n):
        for j in range(m):
            if not board[i][j] and not visited[i][j]:
                s = bfs(i, j)
                road_size[find(get_idx(i, j))] = s
    Map = [each[:] for each in board]
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                Map[i][j] = 1
                side = set()
                for dir in range(4):
                    ni, nj = i + dx[dir], j + dy[dir]
                    if not out_of_bound(ni, nj) and not board[ni][nj]:
                        side.add(find(get_idx(ni, nj)))
                for each in side:
                    Map[i][j] += road_size[each]
    for row in Map:
        for each in row:
            print(each % 10, end='')
        print()

n, m = map(int, input().split())
board = []
visited = [[False] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
parent = [i for i in range(n * m)]
road_size = [0 for _ in range(n * m)]
for _ in range(n):
    board.append(list(map(int ,input().strip())))
solve()