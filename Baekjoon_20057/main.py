import sys

n = int(sys.stdin.readline())
board = []
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
left = [[1, 1, 0.01], [-1, 1, 0.01], [-2, 0, 0.02], [2, 0, 0.02],
        [-1, 0, 0.07], [1, 0, 0.07], [-1, -1, 0.1], [1, -1, 0.1],
        [0, -2, 0.05], [0, -1, 0]]
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(-x, y, z) for x, y, z in down]
rate = [left, down, right, up]
answer = 0

def out_of_bound(x, y):
    return x < 0 or x >= n or y < 0 or y >= n

def make_linear():
    tmp = []
    dir, step = 0, 1

    x, y = n // 2, n // 2
    while True:
        if out_of_bound(x, y): break
        for _ in range(step):
            x, y = x + dx[dir], y + dy[dir]
            if out_of_bound(x, y): break
            tmp.append([x, y, dir])
        dir = (dir + 1) % 4
        if dir % 2 == 0: step += 1
    return tmp

def move_tornado():
    global board, answer
    linear_board = make_linear()
    for x, y, d in linear_board:
        sand, res_sand = board[x][y], board[x][y]
        #printf()
        if not sand: continue
        for each in rate[d]:
            d_x, d_y, r = each
            nx, ny = x + d_x, y + d_y
            if r == 0:
                if out_of_bound(nx, ny): answer += res_sand
                else: board[nx][ny] += res_sand
                break
            if out_of_bound(nx, ny):
                answer += int(sand * r)
                res_sand -= int(sand * r)
            else:
                board[nx][ny] += int(sand * r)
                res_sand -= int(sand * r)
        board[x][y] = 0

def printf():
    for each in board:
        print(*each)
    print()
move_tornado()
#printf()
print(answer)