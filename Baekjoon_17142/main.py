from itertools import combinations
from collections import deque

n, m = map(int, input().split())
lab = []
for _ in range(n):
    lab.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

possible = []
for i in range(n):
    for j in range(n):
        if lab[i][j] == 2:
            possible.append([i, j])

def out_of_bound(x, y):
    if x < 0 or x >= n or y < 0 or y >= n: return True
    return False

def diffusion(each_case):
    cnt = 0
    for row in lab:
        for each in row:
            if each == 0: cnt += 1

    tmp = [each[:] for each in lab]
    dq = deque()
    for x, y in each_case:
        dq.append([x, y, 0])
    elapsed_time = 0
    while dq:
        if cnt <= 0: break
        x, y, t = dq.popleft()
        #print(x, y, t)

        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if not out_of_bound(nx, ny) \
                    and (tmp[nx][ny] == 0 or tmp[nx][ny] == 2):
                dq.append([nx, ny, t + 1])
                elapsed_time = max(elapsed_time, t + 1)
                if tmp[nx][ny] == 0: cnt -=1
                tmp[nx][ny] = -1

    if cnt > 0:
        return -1
    return elapsed_time

res = -1
all_case = combinations(possible, m)
for each_case in all_case:
    t = diffusion(each_case)
    #print(each_case, t)
    if t >= 0:
        if res == -1: res = t
        else: res = min(res, t)
print(res)
