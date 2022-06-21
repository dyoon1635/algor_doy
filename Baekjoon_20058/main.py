import sys
sys.setrecursionlimit(10**5)

n, q = map(int, input().split())
ice = []
n = 2 ** n
for _ in range(n):
    ice.append(list(map(int, input().split())))
L = list(map(int, input().split()))

size = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * (n) for _ in range(n)]

def out_of_bound(x, y):
    if x < 0 or x >= n or \
        y < 0 or y >= n: return True
    return False

def printf():
    for data in ice: print(data)

def local_transform(x, y, size):
    global ice
    local = []
    for i in range(x, x + size): # 기존 local 복사
        tmp = []
        for j in range(y, y + size):
            tmp.append(ice[i][j])
        local.append(tmp)

    for i in range(size): # clockwise rotate
        for j in range(size):
            ice[i + x][j + y] = local[size - j - 1][i]

def rotate(l):
    global ice
    step = 2 ** l
    if step == 1: return None

    for i in range(0, n, step): # 각 grid의 좌상단 (x, y)
        for j in range(0, n, step):
            local_transform(i, j, step)

def melt():
    global ice
    check = [[False] * (n) for _ in range(n)] # 녹을 곳 check
    for i in range(n):
        for j in range(n):
            cnt = 0
            if ice[i][j] <= 0: continue

            for k in range(4):
                nx = i + dx[k] # next x
                ny = j + dy[k] # next y
                if not out_of_bound(nx, ny) and \
                    ice[nx][ny] > 0: cnt += 1
            if cnt < 3: check[i][j] = True

    for i in range(n):
        for j in range(n):
            if check[i][j] and ice[i][j] > 0:
                ice[i][j] -= 1

def bfs(x, y):
    global visited, size
    if out_of_bound(x, y) or \
            visited[x][y] or \
            ice[x][y] <= 0: return 0
    visited[x][y] = True
    size += 1
    for i in range(4):
        bfs(x + dx[i], y + dy[i])

def count():
    global size
    res = 0
    for i in range(n):
        for j in range(n):
            bfs(i, j)
            res = max(res, size)
            size = 0
    return res

if __name__ == "__main__":
    for l in L:
        rotate(l)
        melt()
    total = 0
    for data in ice:
        total += sum(data)
    print(total)
    print(count())
