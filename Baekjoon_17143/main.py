import sys

R, C, M = map(int, sys.stdin.readline().split())
board = [[[] for _ in range(C + 1)] for _ in range(R + 1)]

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

def out_of_bound(x, y):
    return (x < 1 or x > R or y < 1 or y > C)

def shark_move():
    global board
    tmp = [[[] for _ in range(C + 1)] for _ in range(R + 1)]
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            if board[i][j]:
                x, y = i, j
                s, d, z = board[i][j][0]
                dist = s

                if d == 1 or d == 2: dist %= ((R - 1) * 2)
                else: dist %= ((C - 1) * 2)
                while dist > 0:
                    nx, ny = x + dx[d], y + dy[d]
                    if out_of_bound(nx, ny):
                        if d % 2 == 0: d -= 1
                        else: d += 1
                        continue
                    x, y = nx, ny
                    dist -= 1
                tmp[x][y].append([s, d, z])
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            board[i][j] = tmp[i][j]

for _ in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    board[r][c].append([s, d, z])

answer = 0
for col in range(1, C + 1):
    # step 1, 2
    for row in range(1, R + 1):
        if board[row][col]:
            answer += board[row][col][0][-1]
            board[row][col].pop()
            break

    # step 3
    shark_move()
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            if len(board[i][j]):
                board[i][j].sort(key=lambda x: x[2], reverse=True)
            while len(board[i][j]) > 1:
                board[i][j].pop()
print(answer)