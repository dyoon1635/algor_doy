from collections import deque

n = int(input())
area = []
for _ in range(n):
    area.append(list(input()))
visited = [[False] * n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def out_of_bound(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return True
    return False

def set_for_blind():
    global visited
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if area[i][j] == 'R': area[i][j] = 'G'

def bfs(x, y, color):
    global visited
    dq = deque()
    dq.append([x, y])
    while dq:
        cur_x, cur_y = dq.popleft()
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if not out_of_bound(nx, ny) \
                and not visited[nx][ny] \
                and area[nx][ny] == color:
                visited[nx][ny] = True
                dq.append([nx, ny])

def count():
    res = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                res += 1
                bfs(i, j, area[i][j])
    return res

if __name__ == "__main__":
    print(count(), end=' ')
    set_for_blind()
    print(count())