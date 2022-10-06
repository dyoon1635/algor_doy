import sys

n, m = map(int, sys.stdin.readline().split())
A = []
cloud = [[n - 2, 0], [n - 2, 1],
         [n - 1, 0], [n - 1, 1]]
check = [[False] * n for _ in range(n)]
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
for _ in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))

def out_of_bound(x, y):
    return (x < 0 or x >= n or y < 0 or y >= n)

def move_clouds(d, s): # direction, speed
    global A, check
    for x, y in cloud:
        nx, ny = (x + dx[d] * s) % n, (y + dy[d] * s) % n
        A[nx][ny] += 1
        check[nx][ny] = True

def water_copy_bug():
    global A
    tmp = [each[:] for each in A]
    dir_x = [-1, -1, 1, 1]
    dir_y = [-1, 1, -1, 1]
    for i in range(n):
        for j in range(n):
            if check[i][j]:
                cnt = 0
                for dir in range(4):
                    nx, ny = i + dir_x[dir], j + dir_y[dir]
                    if not out_of_bound(nx, ny) and A[nx][ny]:
                        cnt += 1
                tmp[i][j] += cnt
    A = [each[:] for each in tmp]

def make_cloud():
    global cloud, A, check
    del cloud[:]
    for i in range(n):
        for j in range(n):
            if A[i][j] > 1 and not check[i][j]:
                cloud.append([i, j])
                A[i][j] -= 2
    check = [[False] * n for _ in range(n)]

def printf():
    for each in A:
        print(each)
    print()

def SUM():
    res = 0
    for row in A:
        for each in row:
            res += each
    return res

for _ in range(m):
    d, s = map(int, sys.stdin.readline().split())
    move_clouds(d, s)
    water_copy_bug()
    make_cloud()
print(SUM())