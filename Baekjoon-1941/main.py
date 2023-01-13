from itertools import combinations
from collections import deque

def out_of_bound(x, y):
    return x < 0 or x >= 5 or y < 0 or y >= 5

def get_idx(N):
    return [N // 5, N % 5]

def is_connected(case):
    global count
    x, y = get_idx(case[0])
    l = 1
    dq = deque(); dq.append([x, y])
    visited = [[False] * 5 for _ in range(5)]
    visited[x][y] = True

    while dq:
        if l == 7:
            count += 1
            break
        cx, cy = dq.popleft()
        for dir in range(4):
            nx, ny = cx + dx[dir], cy + dy[dir]
            if out_of_bound(nx, ny) or \
                    visited[nx][ny] or \
                    not nx * 5 + ny in case:
                continue
            l += 1
            visited[nx][ny] = True
            dq.append([nx, ny])
    return

def y_count(case):
    y_count = 0
    for each in case:
        x, y = get_idx(each)
        if student[x][y] == 'Y': y_count += 1
        if y_count > 3: return False
    return True

student = []
for i in range(5):
    student.append(list(input()))

idx = [i for i in range(25)]
all_case = combinations(idx, 7)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0
for each_case in all_case:
    if not y_count(each_case): continue
    is_connected(each_case)
print(count)