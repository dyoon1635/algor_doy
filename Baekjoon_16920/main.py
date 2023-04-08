import sys
from collections import deque
input = sys.stdin.readline

def out_of_bound(x, y):
    return not (0 <= x < n and 0 <= y < m)

def bfs():
    while True:
        flag = [False for _ in range(p + 1)]

        for each_player in range(1, p + 1):
            for _ in range(S[each_player]):
                length = len(dq[each_player])
                if length == 0: break
                for _ in range(length):
                    cx, cy = dq[each_player].popleft()
                    for dir in range(4):
                        nx, ny = cx + dx[dir], cy + dy[dir]
                        if not out_of_bound(nx, ny) and board[nx][ny] == '.':
                            flag[each_player] = True
                            board[nx][ny] = each_player
                            castle_count[each_player] += 1
                            dq[each_player].append((nx, ny))
        if True not in flag: break

n, m, p = map(int, input().split())
S = [0] + list(map(int, input().split()))
castle_count = [0 for _ in range(p + 1)]
dq = [deque() for _ in range(p + 1)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = []
for i in range(n):
    tmp = list(input().strip())
    board.append(tmp)

    for idx, each in enumerate(tmp):
        if each != '.' and each != '#':
            tmp[idx] = int(each)
            castle_count[tmp[idx]] += 1
            dq[tmp[idx]].append((i, idx))
bfs()
print(*castle_count[1:])