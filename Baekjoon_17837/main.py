import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
board = [[[] for _ in range(n)] for _ in range(n)]
color = [] # 0 : white, 1 : red, 2 : blue
location = []
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
for _ in range(n):
    color.append(list(map(int, sys.stdin.readline().split())))

for idx in range(k):
    x, y, dir = list(map(int, sys.stdin.readline().split()))
    location.append([x - 1, y - 1, dir])
    board[x - 1][y - 1].append(idx)

def out_of_bound(x, y):
    return (x < 0 or x >= n or y < 0 or y >= n)

def printf():
    for each in board:
        print(each)
    print('')

def check():
    for row in board:
        for each in row:
            if len(each) >= 4:
                return True
    return False

def move(idx, each):
    global board, location
    x, y, dir = each
    nx, ny = x + dx[dir], y + dy[dir]
    if out_of_bound(nx, ny): return False

    tmp_idx = board[x][y].index(idx)
    tmp = board[x][y][tmp_idx:]
    if color[nx][ny] == 0:  # white
        board[nx][ny] += tmp
        del board[x][y][tmp_idx:]
        for num in tmp:
            location[num][0], location[num][1] = nx, ny
        return True
    elif color[nx][ny] == 1:  # red
        board[nx][ny] += reversed(tmp)
        del board[x][y][tmp_idx:]
        for num in tmp:
            location[num][0], location[num][1] = nx, ny
        return True
    return False

turn = 0
while turn <= 1000:
    turn += 1
    #printf()
    for idx, each in enumerate(location):
        if not move(idx, each):
            if location[idx][-1] % 2 == 0: location[idx][-1] -= 1
            else: location[idx][-1] += 1
            move(idx, location[idx])
        if check():
            print(turn)
            exit(0)
print(-1)
