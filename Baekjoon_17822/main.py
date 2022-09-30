import sys, math
from collections import deque

n, m, t = map(int, sys.stdin.readline().split())
inf = 1000000
board = [deque([inf] * m)]
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    board.append(deque(tmp))
board.append(deque([inf] * m))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def out_of_bound(x, y):
    return x < 1 or x > n or y < 0 or y >= m

def condition(x, y):
    return (x == y and x != inf and y != inf)

def total(check):
    for i in range(1, n + 1):
        for j in range(m):
            if check[i][j]: return -1
    total, cnt = 0, 0
    for i in range(1, n + 1):
        for j in range(m):
            if board[i][j] == inf: continue
            total += board[i][j]
            cnt += 1
    if cnt > 0:
        return total / cnt
    return -1

def printf():
    for each in board:
        print(each)

def erase():
    global board
    check = [[False] * m for _ in range(1 + n)]
    # 지울 원판 부분 check
    for i in range(1, n + 1):
        for j in range(m):
            for dir in range(4):
                nx, ny = i + dx[dir], j + dy[dir]
                if out_of_bound(nx, ny): continue
                if condition(board[i][j], board[nx][ny]):
                    check[i][j], check[nx][ny] = True, True
        if condition(board[i][0], board[i][-1]):
            check[i][0], check[i][-1] = True, True
    # erase
    for i in range(1, n + 1):
        for j in range(m):
            if check[i][j]:
                board[i][j] = inf
    # avg
    avg = total(check)
    if avg != -1:
        for i in range(1, n + 1):
            for j in range(m):
                if board[i][j] == inf: continue
                if board[i][j] < avg: board[i][j] += 1
                elif board[i][j] > avg : board[i][j] -= 1

for _ in range(t):
    x, d, k = map(int, sys.stdin.readline().split())
    tmp = x
    while tmp <= n:
        board[tmp].rotate(k * pow(-1, d))
        tmp += x
    erase()
result = 0
for row in board:
    for each in row:
        if each == inf: continue
        result += each
print(result)
