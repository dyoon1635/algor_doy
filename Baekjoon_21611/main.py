import sys

def out_of_bound(x, y):
    return x < 1 or x > n or y < 1 or y > n

def make_linear():
    dir_x = [0, 1, 0, -1]
    dir_y = [-1, 0, 1, 0]
    tmp = [[s_x, s_y]]
    cnt, d, step = 1, 0, 1
    x, y = s_x, s_y
    while True:
        if cnt > n ** 2: break
        for _ in range(step):
            x, y = x + dir_x[d], y + dir_y[d]
            if out_of_bound(x, y): break
            tmp.append([x, y])
            cnt += 1
        d = (d + 1) % 4
        if d % 2 == 0: step += 1
    return tmp
linear_board = make_linear()

def blizard_spell(d, s):
    global board, count
    x, y = s_x + dx[d], s_y + dy[d]
    while not out_of_bound(x, y) and s > 0:
        board[x][y] = 0
        x, y = x + dx[d], y + dy[d]
        s -= 1

def move_beads():
    global board
    start, end = 1, 2
    sx, sy, ex, ey = 0, 0, 0, 0
    while start < n ** 2 and end <= n ** 2:
        while start < n ** 2:
            sx, sy = linear_board[start]
            if not board[sx][sy]: break
            start += 1
        if start == n ** 2: return

        if end <= start: end = start + 1
        while end <= n ** 2:
            ex, ey = linear_board[end]
            if board[ex][ey]: break
            end += 1
        if end == n ** 2: return
        board[sx][sy], board[ex][ey] = board[ex][ey], 0

def count_consecutive_beads():
    check = [1] * (n ** 2)
    for i in range(1, n ** 2):
        ex, ey = linear_board[i - 1]
        x, y = linear_board[i]
        if board[ex][ey] == board[x][y] and board[x][y]:
            check[i] = check[i - 1] + 1
    return check

def explode_beads():
    global board
    exploded = False
    check = count_consecutive_beads()
    i = n ** 2 - 1
    while i >= 0:
        if check[i] >= 4:
            exploded = True
            x, y = linear_board[i]
            count[board[x][y]] += check[i]
            for j in range(check[i]):
                x, y = linear_board[i - j]
                board[x][y] = 0
            i -= check[i]
            continue
        i -= 1
    return exploded

def change_beads():
    global board
    tmp = [[0] * (n + 1) for _ in range(n + 1)]
    check = count_consecutive_beads()
    beads = []

    i = n ** 2 - 1
    while i > 0:
        x, y = linear_board[i]
        if board[x][y]:
            beads.append([check[i], board[x][y]])
            i -= check[i]
            continue
        i -= 1

    idx = 1
    for each in reversed(beads):
        cnt, num = each
        if idx + 2 > n ** 2: break

        x1, y1 = linear_board[idx]
        x2, y2 = linear_board[idx + 1]
        tmp[x1][y1], tmp[x2][y2] = cnt, num
        idx += 2
    board = [each[:] for each in tmp]

def SUM():
    result = 0
    for i in range(1, 4):
        result += (count[i] * i)
    return result

def printf():
    for idx, each in enumerate(board):
        if idx == 0: continue
        print(each[1:])
    print()

n, m = map(int, sys.stdin.readline().split())
board = [[0] * (n + 1)]
s_x, s_y = int((n + 1) / 2), int((n + 1) / 2)
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
count = [0, 0, 0, 0]
for _ in range(n):
    board.append([0] + list(map(int, sys.stdin.readline().split())))

for _ in range(m):
    d, s = map(int, sys.stdin.readline().split())
    blizard_spell(d, s)
    move_beads()
    while explode_beads():
        move_beads()
    change_beads()
print(SUM())

