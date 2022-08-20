from collections import deque

n = int(input())
field = []
sx, sy, size = -1, -1, 2
count, fish_count = 0, 0
for i in range(n):
    tmp = list(map(int, input().split()))
    field.append(tmp)
    for j in range(n):
        if tmp[j] == 9:
            sx, sy = i, j
            field[i][j] = 0
visited = [[False] * n for _ in range(n)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def out_of_bound(x, y):
    if x < 0 or x >= n or y < 0 or y >= n: return True
    return False

def bfs():
    global visited
    visited = [[False] * n for _ in range(n)]
    dq, fish = deque(), []
    dq.append([sx, sy, 0])
    visited[sx][sy] = True
    while dq:
        x, y, dist = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            #print(nx, ny)
            if not out_of_bound(nx, ny) and not visited[nx][ny] and field[nx][ny] <= size:
                if 0 < field[nx][ny] < size:
                    fish.append([nx, ny, dist + 1])
                visited[nx][ny] = True
                dq.append([nx, ny, dist + 1])
    return fish

if __name__ == "__main__":
    while True:
        fish = bfs()
        if not fish: break
        fish.sort(key=lambda x: (x[2], x[0], x[1]))
        sx, sy, dist = fish[0]
        field[sx][sy] = 0
        count += dist
        fish_count += 1
        if fish_count == size:
            size += 1
            fish_count = 0
    print(count)