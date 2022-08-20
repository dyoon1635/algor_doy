import copy

fishes = []
field = [[0] * 4 for _ in range(4)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
for i in range(4):
    tmp = list(map(int, input().split()))
    a, b = tmp[::2], tmp[1::2]
    for j in range(4):
        fishes.append([a[j], b[j] - 1, i , j]) # fish, dir, x, y
        field[i][j] = a[j]
sx, sy,  = 0, 0
sdir, score = fishes[0][1], fishes[0][0]
fishes[0][2], fishes[0][3] = -1, -1

field[0][0] = -1 # shark's location
fishes.append([0, -1, -1, -1])
fishes.sort()

def out_of_bound(x, y):
    if x < 0 or x >= 4 or y < 0 or y >= 4: return True
    return False

def shark_move():
    pass

def fish_move(data, board):
    fishes, field = copy.deepcopy(data), copy.deepcopy(board)
    for each in range(1, 16):
        fish, dir, x, y = each
        if x == -1 or y == -1: continue

        moved, count = False, 0
        while not moved:
            if count == 8: break
            nx, ny = x + dx[dir], y + dy[dir]
            if not out_of_bound(nx, ny) and field[nx][ny] != -1:
                fishes[fish][1], fishes[fish][2], fishes[fish][3] = dir, nx, ny
                field[x][y], field[nx][ny] = field[nx][ny], field[x][y]
                if field[x][y]:
                    fishes[field[x][y]][2], fishes[field[x][y]][3] = x, y
                moved = True
            count += 1
            dir = (dir + count) % 8
    return fishes, board