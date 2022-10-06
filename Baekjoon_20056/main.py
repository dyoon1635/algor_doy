n, m, k = map(int, input().split())
board = [[[] for _ in range(1 + n)] for _ in range(1 + n)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    board[r][c].append([m, s, d]) # mass, speed, dir

def new_direction(arr):
    even_num, odd_num = False, False
    for m, s, d in arr:
        if d % 2 == 0: even_num = True
        else: odd_num = True
    if even_num and odd_num: return [1, 3, 5, 7]
    return [0, 2, 4, 6]

def split_fireball():
    global board
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if len(board[i][j]) > 1:
                new_m, new_s, new_d = 0, 0, new_direction(board[i][j])
                for m, s, d in board[i][j]:
                    new_m += m
                    new_s += s
                new_m, new_s = int(new_m / 5), int(new_s / len(board[i][j]))
                board[i][j] = []
                if new_m == 0: continue
                for dir in new_d:
                    board[i][j].append([new_m, new_s, dir])

def move_fireball():
    global board
    tmp = [[[] for _ in range(1 + n)] for _ in range(1 + n)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if board[i][j]:
                for each in board[i][j]:
                    m, s, d = each
                    nx, ny = (i + dx[d] * s) % n + 1, (j + dy[d] * s) % n + 1
                    tmp[nx][ny].append([m, s, d])
    board = [each[:] for each in tmp]

def get_mass():
    mass = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if board[i][j]:
                for each in board[i][j]:
                    mass += each[0]
    return mass


for _ in range(k):
    move_fireball()
    split_fireball()
print(get_mass())
